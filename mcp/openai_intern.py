import os
import sys

from fastmcp import FastMCP
from openai import OpenAI

mcp = FastMCP(name="openai-intern")
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
MODEL = os.environ.get("OPENAI_MODEL", "o3")


def _call(system_prompt: str, user_prompt: str) -> str:
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_prompt})
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_completion_tokens=16384,
    )
    return response.choices[0].message.content


def _system(role_context: str) -> str:
    base = "You are a helpful AI assistant acting as an intern to a specialist agent."
    if role_context:
        base += f" The specialist you assist describes themselves as: {role_context}"
    return base


@mcp.tool
def ask(prompt: str, role_context: str = "", output_format: str = "markdown") -> str:
    """Ask the OpenAI intern a question or give it a task. General-purpose tool for
    research, analysis, brainstorming, or any free-form query."""
    system = _system(role_context) + f"\n\nRespond in {output_format} format."
    return _call(system, prompt)


@mcp.tool
def draft(
    instructions: str,
    content_type: str,
    role_context: str = "",
    tone: str = "professional",
    length: str = "medium",
) -> str:
    """Have the OpenAI intern draft content: code, documentation, emails, reports,
    proposals, blog posts, scripts, or any other written material."""
    system = _system(role_context)
    system += f"\n\nYou are drafting {content_type} content. Tone: {tone}. Target length: {length}."
    return _call(system, instructions)


@mcp.tool
def review(
    content: str,
    review_type: str,
    criteria: str = "",
    role_context: str = "",
) -> str:
    """Have the OpenAI intern review and critique content or code. Useful for code review,
    security audit, copy editing, compliance checks, or quality assurance."""
    system = _system(role_context)
    system += f"\n\nPerform a {review_type} review."
    if criteria:
        system += f" Evaluate against these criteria: {criteria}"
    return _call(system, f"Review the following:\n\n{content}")


@mcp.tool
def analyze(
    subject: str,
    data: str = "",
    analysis_type: str = "general",
    role_context: str = "",
) -> str:
    """Have the OpenAI intern perform structured analysis on data, scenarios, or problems.
    Supports cost-benefit, risk, competitive, root-cause, trend, comparison, and feasibility analysis."""
    system = _system(role_context)
    system += f"\n\nPerform a {analysis_type} analysis. Be structured and thorough."
    user_msg = f"Analyze: {subject}"
    if data:
        user_msg += f"\n\nData/Context:\n{data}"
    return _call(system, user_msg)


@mcp.tool
def brainstorm(
    topic: str,
    num_ideas: int = 5,
    constraints: str = "",
    role_context: str = "",
) -> str:
    """Have the OpenAI intern generate ideas, alternatives, or creative options for a topic."""
    system = _system(role_context)
    system += f"\n\nGenerate exactly {num_ideas} distinct ideas or options."
    if constraints:
        system += f" Constraints: {constraints}"
    return _call(system, f"Brainstorm about: {topic}")


if __name__ == "__main__":
    mcp.run()
