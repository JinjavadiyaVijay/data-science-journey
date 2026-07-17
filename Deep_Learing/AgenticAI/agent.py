from pathlib import Path
from agno.agent import Agent
from agno.tools.workspace import Workspace
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

def build_agent():
    return Agent(
        model = Groq(id="qwen/qwen3-32b"),
        instructions ="you are famous stand-up comdain",
        markdown = True,

    )

agent = build_agent()
agent.print_response("tell me dark double meaning jokes")
