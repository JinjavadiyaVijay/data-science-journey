from pathlib import Path
from agno.agent import Agent
from agno.tools.workspace import Workspace
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools 
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
load_dotenv()

def build_agent():
    return Agent(
        model = Groq(id="qwen/qwen3.6-27b"),
        tools= [DuckDuckGoTools(),YFinanceTools()],
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible. use all tools if possible, give me accurate answer"],
        #instructions ="you are famous stand-up comdain",
        markdown = True,
        add_datetime_to_context=True,
        debug = True
    )

agent = build_agent()
agent.print_response("wht is starting CTC for recently pass out diploma student with some good project and skills ")
