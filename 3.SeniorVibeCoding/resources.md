Here is your structured Reading & Study Guide. It organizes all 15 resources into a clear, prioritized learning roadmap so you can go from foundational agent concepts to advanced multi-agent steering without getting overwhelmed by reading everything at once.

---

# AI Agent Mastery: Reading & Study Roadmap

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      PHASE 1: THE FOUNDATIONS                          │
 │     Understand token costs, context drift, and agent harnesses        │
 └──────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │                   PHASE 2: PROJECT RULES & STEERING                    │
 │         Master AGENTS.md, CLAUDE.md, and rule configuration           │
 └──────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │                 PHASE 3: PRACTICAL VIBE CODING & DEEP DIVE             │
 │        Advanced multi-agent workflows, Cursor, and AutoResearch       │
 └────────────────────────────────────────────────────────────────────────┘

```

---

## Phase 1: Foundational Mechanics (High Priority)

*Start here to understand why agents behave the way they do, how token budgets get consumed, and how basic ReAct loops operate under the hood.*

### 1. Token Optimization & Context Management

* **Resource:** [Sombra Inc — Token Optimization](https://sombrainc.com/blog/token-optimization) -- too much focused on development of agents token saving so may not be that helpful, not sure, this info was already covered by llm too
* **Priority:** 🔴 **CRITICAL (Read First)**
* **What it teaches:** Introduces the concept of **"agent suicide by context"**—how agents spend thousands of tokens re-reading terminal output and context history until their reasoning degrades. It establishes the mathematical and architectural reasons behind token compaction, sub-task resets, and why fresh execution threads are necessary.

### 2. Agentic Loops Explained

* **Resource:** [Data Science Dojo — Agentic Loops Explained: From ReAct to Loop Engineering](https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/)
* **Priority:** 🔴 **CRITICAL**
* **What it teaches:** Breaks down the fundamental mechanics of agent loops (Reason + Act). Explains the basic requirements of an autonomous loop: an execution goal, tools (file edit, bash, search), and a deterministic evaluation loop that checks work and continues.

### 3. OpenAI Codex Architecture & Harness Basics

* **Resources:**
* [SWE Quiz — OpenAI Codex Architecture](https://swequiz.com/articles/openai-codex-architecture)
* [Gend — Codex Agent Loop Enhances AI Efficiency](https://www.gend.co/blog/codex-agent-loop-enhances-ai-efficiency)
* [The Neuron — From Zero to Codex Hero](https://www.theneuron.ai/explainer-articles/from-zero-to-codex-hero-everything-you-need-to-know-about-openais-coding-agent/)


* **Priority:** 🟡 **HIGH**
* **What they teach:** Gives you an inside look at how Codex operates under the hood. Explains how OpenAI manages context compaction, execution sandboxes, and tool calls automatically so you don't have to build custom harnesses from scratch.

---

## Phase 2: Project Steering & Configuration Rules (High Priority)

*Read these to master `AGENTS.md` and understand how to enforce your custom workflow across Codex, Claude Code, and Cursor.*

### 4. The Core AGENTS.md Concept

* **Resources:**
* [Verdent AI — Codex AGENTS.md Explained](https://www.verdent.ai/guides/codex-agents-md-explained)
* [Kingy AI — The Definitive Guide to AGENTS.md](https://kingy.ai/news/the-definitive-guide-to-agents-md-what-it-is-how-to-use-it-and-why-it-matters/)
* [ChatGPT Learn — Agent Configuration: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)


* **Priority:** 🔴 **CRITICAL**
* **What they teach:** Explains the file discovery hierarchy of `AGENTS.md` (how local rules override global rules), how LLMs parse Markdown guardrails, and how to write precise prompt constraints that steer agent behavior without wasting context.

### 5. Practical Setup & Cross-Platform Rules Comparison

* **Resources:**
* [Sulat AI — Codex CLI Quick Start & AGENTS.md Guide](https://ai.sulat.com/codex-cli-quick-start-agents-md-better-prompts-safer-runs-36d7060fcf68)
* [Easton Dev — Codex Project Rules Configuration](https://eastondev.com/blog/en/posts/ai/20260626-codex-agents-md-project-rules/)
* [Codersera — AGENTS.md vs CLAUDE.md vs Cursor Rules Comparison](https://codersera.com/blog/agents-md-vs-claude-md-vs-cursor-rules-comparison-2026/)
* [arXiv (2606.15828v3) — Standardizing Agent Configuration Files](https://arxiv.org/html/2606.15828v3)


* **Priority:** 🟡 **HIGH**
* **What they teach:** Compares how different tools read system instructions (`AGENTS.md` for Codex, `CLAUDE.md` for Anthropic, `.cursor/rules/*.mdc` for Cursor). Teaches you how to create universal rules files or use symlinks so your workflow works seamlessly across all platforms.

---

## Phase 3: Advanced Workflows, Cursor & AutoResearch (Medium / Optional Priority)

*Diver into these once your basic setup is running to explore parallel multi-agent setups and optimization techniques.*

### 6. Senior Vibe Coding & Claude Code Capabilities

* **Resources:**
* [Agentman AI — Mastering Vibe Coding: Advanced Techniques](https://agentman.ai/blog/mastering-vibe-coding-advanced-techniques)
* [HatchWorks — Claude Code Agentic Workflow Guide](https://hatchworks.com/blog/claude/claude-code/)


* **Priority:** 🟢 **MEDIUM**
* **What they teach:** Focuses on human-agent collaboration patterns ("Senior Vibe Coding"). Covers phase-gating, manual approval checkpoints, and end-to-end task execution in Claude Code's terminal environment.

### 7. Multi-Agent Systems & AutoResearch Concepts

* **Resources:**
* [DEV Community — Cursor Parallel AI Agents & Workflows](https://dev.to/thegdsks/cursor-3-ships-parallel-ai-agents-here-is-the-multi-agent-workflow-that-actually-works-2bk8)
* [Verdent AI — What is AutoResearch by Karpathy?](https://www.verdent.ai/guides/what-is-autoresearch-karpathy)


* **Priority:** ⚪ **OPTIONAL / ADVANCED**
* **What they teach:**
* **Cursor Parallel Agents:** Shows how to run parallel subagents in Cursor's UI for multi-repo or multi-feature tasks.
* **AutoResearch:** Explains Andrej Karpathy's experimental framework for autonomous optimization loops (one file, one quantitative evaluation metric, looping indefinitely until performance improves).



---

## Suggested Reading Order Checklist

* [ ] **Step 1:** Read *Sombra Inc (Token Optimization)* to understand token constraints.
* [ ] **Step 2:** Read *Data Science Dojo (Agentic Loops)* to understand ReAct loops.
* [ ] **Step 3:** Read *Kingy AI* & *Verdent AI (AGENTS.md Explained)* to master rule configuration.
* [ ] **Step 4:** Read *Codersera (AGENTS.md vs CLAUDE.md)* to see how rules apply across different tools.
* [ ] **Step 5:** Skim *Agentman AI (Vibe Coding)* and *DEV Community (Cursor Parallel Agents)* when you are ready to prepare your meetup demonstration.