from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model = Groq(id="qwen/qwen3.6-27b"),
        markdown = True,
        add_history_to_context=True,
        enable_agentic_memory =True,
        enable_user_memories = True
#        update_memory_on_run =True # can used update_memory or Agentic memory(can't use both at a time)

    )
agent = build_agent()

user_id = "jinjavadiyavijayy8@gmail.com"
agent.print_response("i am vijay and im ai engineer, i work at ramora technologies as intern",user_id=user_id)
agent.print_response("who am i?",user_id=user_id)

memories = agent.get_user_memories(
    user_id = user_id
)
print("Memories: ")
pprint(memories)