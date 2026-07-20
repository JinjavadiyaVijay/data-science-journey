from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

eng_agent = Agent(name="English Agent ", role = "you answer question in english") 
chi_agent=Agent(name="chinese Agent ", role = "you answer question in chinese") 
hindi_agent=Agent(name="Hindi Agent ", role = "you answer question in hindi") 

team = Team(
    name = "answe & Ttansalteion team",
    members = [eng_agent,chi_agent,hindi_agent],
    model = Groq(id="qwen/qwen3.6-27b"),
    instructions = """
    All member agents must respond to answer the query in their specific 
    langauge.Do not call just one agent,
    Output the response of all agent """,
    markdown =True,
    show_members_responses= True
)

team.print_response("what is tha capital of india")
