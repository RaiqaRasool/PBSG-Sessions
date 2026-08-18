import argparse
import asyncio
import json
import os
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from openai import AsyncOpenAI

READ_RESOURCE_TOOL_NAME = "read_mcp_resource"
INSTRUCTIONS = (
    "Answer the user's question. Use the available functions when the question "
    "requires current information from MCP."
)

ResourceCatalog = dict[str, Any]
ToolCatalog = dict[str, Any]
ModelTool = dict[str, Any]
ModelInput = list[Any]


def parse_question() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("question", help="Question for the local agent")
    return parser.parse_args().question


def create_llm_client() -> tuple[AsyncOpenAI, str]:
    model = os.environ.get("LM_STUDIO_MODEL")
    if not model:
        raise RuntimeError("Set LM_STUDIO_MODEL to the loaded LM Studio model ID")

    client = AsyncOpenAI(
        base_url=os.environ.get(
            "OPENAI_BASE_URL", "http://host.docker.internal:1234/v1"
        ),
        api_key=os.environ.get("OPENAI_API_KEY", "lm-studio"),
    )
    return client, model


def create_mcp_server() -> StdioServerParameters:
    return StdioServerParameters(
        command="python",
        args=["/phoenix/server.py"],
    )


async def initialize_mcp_session(session: ClientSession) -> None:
    print("[MCP CLIENT -> MCP SERVER] initialize")
    result = await session.initialize()
    print(
        "[MCP SERVER -> MCP CLIENT] initialize result "
        f"server={result.serverInfo.name} version={result.serverInfo.version}"
    )


async def discover_resources(session: ClientSession) -> ResourceCatalog:
    print("[MCP CLIENT -> MCP SERVER] resources/list")
    result = await session.list_resources()

    catalog = {str(resource.uri): resource for resource in result.resources}
    print("[MCP SERVER -> MCP CLIENT] resources/list result")
    for uri, resource in catalog.items():
        print(f"  - uri={uri} name={resource.name}")

    if not catalog:
        raise RuntimeError("Server did not advertise any resources")
    return catalog


async def discover_tools(session: ClientSession) -> ToolCatalog:
    print("[MCP CLIENT -> MCP SERVER] tools/list")
    result = await session.list_tools()

    catalog = {tool.name: tool for tool in result.tools}
    print("[MCP SERVER -> MCP CLIENT] tools/list result")
    for tool in result.tools:
        print(f"  - name={tool.name}")
    return catalog


def build_read_resource_tool(resource_catalog: ResourceCatalog) -> ModelTool:
    catalog_description = "; ".join(
        f"{uri} ({resource.name})" for uri, resource in resource_catalog.items()
    )
    return {
        "type": "function",
        "name": READ_RESOURCE_TOOL_NAME,
        "description": (
            "Read one resource advertised by the connected MCP server. "
            f"Available resources: {catalog_description}"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "uri": {
                    "type": "string",
                    "description": "URI of the resource to read.",
                    "enum": list(resource_catalog),
                }
            },
            "required": ["uri"],
            "additionalProperties": False,
        },
        "strict": True,
    }


def build_mcp_tools(tool_catalog: ToolCatalog) -> list[ModelTool]:
    model_tools = []
    for tool in tool_catalog.values():
        parameters = dict(tool.inputSchema)
        parameters["additionalProperties"] = False
        model_tools.append(
            {
                "type": "function",
                "name": tool.name,
                "description": tool.description or f"Call MCP tool {tool.name}.",
                "parameters": parameters,
                "strict": True,
            }
        )
    return model_tools


async def request_model_decision(
    client: AsyncOpenAI,
    model: str,
    question: str,
    tools: list[ModelTool],
) -> tuple[Any, ModelInput]:
    input_items: ModelInput = [{"role": "user", "content": question}]
    print(f"[AGENT -> MODEL] request tools={[tool['name'] for tool in tools]}")

    response = await client.responses.create(
        model=model,
        instructions=INSTRUCTIONS,
        tools=tools,
        input=input_items,
    )
    input_items += response.output

    for item in response.output:
        print(f"[MODEL -> AGENT] output item type={item.type}")
    return response, input_items


def select_function_call(response: Any) -> Any | None:
    function_calls = [
        item for item in response.output if item.type == "function_call"
    ]
    if not function_calls:
        return None
    if len(function_calls) > 1:
        raise RuntimeError("Model requested more than one function call")

    function_call = function_calls[0]
    print("[MODEL -> AGENT] function call")
    print(f"  name={function_call.name}")
    print(f"  arguments={function_call.arguments}")
    return function_call


def validate_resource_call(
    function_call: Any,
    resource_catalog: ResourceCatalog,
) -> str:
    if function_call.name != READ_RESOURCE_TOOL_NAME:
        raise RuntimeError(
            f"Model requested unsupported function {function_call.name}"
        )

    arguments = json.loads(function_call.arguments)
    if set(arguments) != {"uri"} or not isinstance(arguments["uri"], str):
        raise RuntimeError(
            f"{READ_RESOURCE_TOOL_NAME} requires one string uri argument"
        )

    uri = arguments["uri"]
    if uri not in resource_catalog:
        raise RuntimeError(f"Model requested unadvertised resource {uri}")
    return uri


def validate_mcp_tool_call(
    function_call: Any,
    tool_catalog: ToolCatalog,
) -> tuple[str, dict[str, Any]]:
    tool = tool_catalog.get(function_call.name)
    if tool is None:
        raise RuntimeError(
            f"Model requested unsupported function {function_call.name}"
        )

    arguments = json.loads(function_call.arguments)
    if not isinstance(arguments, dict):
        raise RuntimeError(f"{function_call.name} arguments must be an object")

    schema = tool.inputSchema
    properties = schema.get("properties", {})
    required = set(schema.get("required", []))
    if (
        not required <= arguments.keys()
        or not arguments.keys() <= properties.keys()
    ):
        raise RuntimeError(
            f"{function_call.name} arguments do not match its advertised schema"
        )
    for name, value in arguments.items():
        expected_type = properties[name].get("type")
        if expected_type == "string" and not isinstance(value, str):
            raise RuntimeError(f"{function_call.name}.{name} must be a string")
    return function_call.name, arguments


async def read_mcp_resource(session: ClientSession, uri: str) -> str:
    print(f"[AGENT] Mapping {READ_RESOURCE_TOOL_NAME} to MCP resources/read")
    print(f"[MCP CLIENT -> MCP SERVER] resources/read uri={uri}")
    result = await session.read_resource(uri)
    contents = json.dumps(
        [
            content.model_dump(mode="json", by_alias=True)
            for content in result.contents
        ],
        indent=2,
    )
    print("[MCP SERVER -> MCP CLIENT] resources/read result")
    print(contents)
    return contents


async def call_mcp_tool(
    session: ClientSession,
    name: str,
    arguments: dict[str, Any],
) -> str:
    print(f"[AGENT] Mapping model function {name} to MCP tools/call")
    print(f"[MCP CLIENT -> MCP SERVER] tools/call name={name}")
    result = await session.call_tool(name, arguments)
    output = json.dumps(
        result.model_dump(mode="json", by_alias=True),
        indent=2,
    )
    print("[MCP SERVER -> MCP CLIENT] tools/call result")
    print(output)
    return output


async def request_final_answer(
    client: AsyncOpenAI,
    model: str,
    tools: list[ModelTool],
    input_items: ModelInput,
    call_id: str,
    function_output: str,
) -> str:
    input_items.append(
        {
            "type": "function_call_output",
            "call_id": call_id,
            "output": function_output,
        }
    )
    print(f"[AGENT -> MODEL] function_call_output call_id={call_id}")

    response = await client.responses.create(
        model=model,
        instructions=INSTRUCTIONS,
        tools=tools,
        input=input_items,
    )
    print("[MODEL -> AGENT] final response")
    return response.output_text


async def run_agent(
    session: ClientSession,
    client: AsyncOpenAI,
    model: str,
    question: str,
) -> str:
    resource_catalog = await discover_resources(session)
    tool_catalog = await discover_tools(session)
    model_tools = [
        build_read_resource_tool(resource_catalog),
        *build_mcp_tools(tool_catalog),
    ]
    response, input_items = await request_model_decision(
        client,
        model,
        question,
        model_tools,
    )

    function_call = select_function_call(response)
    if function_call is None:
        print("[AGENT] Model answered without MCP")
        return response.output_text

    if function_call.name == READ_RESOURCE_TOOL_NAME:
        uri = validate_resource_call(function_call, resource_catalog)
        function_output = await read_mcp_resource(session, uri)
    else:
        name, arguments = validate_mcp_tool_call(function_call, tool_catalog)
        function_output = await call_mcp_tool(session, name, arguments)
    return await request_final_answer(
        client,
        model,
        model_tools,
        input_items,
        function_call.call_id,
        function_output,
    )


async def main() -> None:
    question = parse_question()
    llm_client, model = create_llm_client()
    mcp_server = create_mcp_server()

    print(f"[USER -> AGENT] {question}")
    print("[MCP CLIENT] Launching MCP server child process over stdio")
    with open(os.devnull, "w", encoding="utf-8") as server_stderr:
        async with stdio_client(
            mcp_server,
            errlog=server_stderr,
        ) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await initialize_mcp_session(session)
                answer = await run_agent(session, llm_client, model, question)

    print("[AGENT -> USER]")
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())
