from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()

db = SqliteDb("agno.db")

youtube_agent = Agent(
    name="YouTube analyzer",
    markdown=True,
    tools=[YouTubeTools()],
    model=Groq(id="llama-3.3-70b-versatile"),
    db=db,
    debug_mode=True,
    instructions=dedent("""
    You are an expert YouTube content analyzer.

    Analyze the video objectively using available YouTube metadata, captions, and timestamps.

    Return:
    1. Video overview:
       - Length and metadata
       - Video type
       - Main topic
       - Target audience
       - Overall purpose

    2. Timestamped breakdown:
       - Format: [start_time, end_time, detailed_summary]
       - Focus on major topic transitions
       - Highlight key moments and demonstrations
       - Skip intros and low-value sections when possible

    3. Content organization:
       - Main themes
       - Topic progression
       - Important examples and conclusions

    4. Key extraction:
       - Actionable insights
       - People, companies, products, books, or technologies mentioned
       - Facts vs opinions
    """),
    add_datetime_to_context=True,
)

youtube_agent.print_response(
    "Analyze this video: https://youtu.be/glyPKGwrauk?si=IUhqd-BZg3ga7SqJ",
    stream=False,
)