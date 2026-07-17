from pathlib import Path
from agno.agent import Agent
from agno.tools.workspace import Workspace
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools 

from dotenv import load_dotenv
load_dotenv()

def build_agent():
    return Agent(
        model = Groq(id="qwen/qwen3-32b"),
        tools= [DuckDuckGoTools()],
        #instructions ="you are famous stand-up comdain",
        markdown = True,
        add_datetime_to_context=True,



    )

agent = build_agent()
agent.print_response("wht is starting CTC for recently pass out diploma student with some good project and skills ")
