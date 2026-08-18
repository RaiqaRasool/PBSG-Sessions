from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Literal

from mcp.server.fastmcp import FastMCP


STATUS_FILE = Path(__file__).with_name("project-status.md")

mcp = FastMCP("Project Status")


@mcp.resource("project://phoenix/status", mime_type="text/markdown")
def get_project_status() -> str:
    """Return the current Project Phoenix status as Markdown."""
    try:
        return STATUS_FILE.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise RuntimeError(f"Unable to read project status: {exc}") from exc


@mcp.tool()
def find_project_updates(author: str) -> str:
    """Return Project Phoenix updates written by one author."""
    clean_author = author.strip()
    if not clean_author:
        raise ValueError("author must contain non-whitespace text")
    if "\n" in clean_author or "\r" in clean_author:
        raise ValueError("author must be a single line")

    try:
        status = STATUS_FILE.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise RuntimeError(f"Unable to read project status: {exc}") from exc

    sections = re.findall(
        rf"^### \d{{4}}-\d{{2}}-\d{{2}} — {re.escape(clean_author)}\n\n.*?(?=^### |\Z)",
        status,
        flags=re.MULTILINE | re.DOTALL,
    )
    return "\n".join(section.rstrip() for section in sections) or (
        f"No project updates found for {clean_author}."
    )


@mcp.tool()
def add_project_update(update: str, author: str) -> str:
    """Append a dated update to the Project Phoenix status file."""
    clean_update = update.strip()
    clean_author = author.strip()

    if not clean_update:
        raise ValueError("update must contain non-whitespace text")
    if not clean_author:
        raise ValueError("author must contain non-whitespace text")
    if "\n" in clean_author or "\r" in clean_author:
        raise ValueError("author must be a single line")

    update_date = datetime.now(timezone.utc).date().isoformat()
    entry = f"\n### {update_date} — {clean_author}\n\n{clean_update}\n"

    try:
        with STATUS_FILE.open("a", encoding="utf-8") as status_file:
            status_file.write(entry)
    except OSError as exc:
        raise RuntimeError(f"Unable to append project update: {exc}") from exc

    return f"Added project update from {clean_author} on {update_date}."


@mcp.prompt()
def prepare_status_review(
    audience: Literal["engineering", "leadership"],
    focus: Literal["blockers", "progress", "risks"],
) -> str:
    """Prepare a Project Phoenix review.

    Audience must be engineering or leadership. Focus must be blockers,
    progress, or risks.
    """
    audience_guidance = {
        "engineering": (
            "Use implementation detail. Highlight dependencies, owners, and "
            "concrete next actions."
        ),
        "leadership": (
            "Be concise. Emphasize outcomes, impact, decisions, and items that "
            "need escalation."
        ),
    }
    focus_guidance = {
        "blockers": "Prioritize active blockers, their effects, and what can unblock them.",
        "progress": "Prioritize completed work, current momentum, and the next milestone.",
        "risks": "Prioritize uncertainties, likelihood, impact, and possible mitigations.",
    }

    return (
        "Read the MCP resource project://phoenix/status, then prepare a Project "
        f"Phoenix status review for {audience}. {audience_guidance[audience]} "
        f"Focus on {focus}. {focus_guidance[focus]} Base the review only on the "
        "resource content, and clearly label missing information instead of "
        "inventing details."
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
