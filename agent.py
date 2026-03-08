from __future__ import annotations
from livekit.agents import (
    Agent,
    AgentSession,
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
    llm,
    function_tool,
    RunContext
)
from livekit.plugins import openai
from dotenv import load_dotenv
from backend.api import AssistantFnc
from backend.prompts import WELCOME_MESSAGE, INSTRUCTIONS, LOOKUP_VIN_MESSAGE
import os

load_dotenv()

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL) #Subscribe means it will Subscribe all tracks(video,audio)
    
    # Create the function context
    assistant_fnc = AssistantFnc()
    # Create the agent with instructions and tools
    agent = Agent(
        instructions=INSTRUCTIONS,
        tools=[
            assistant_fnc.lookup_car,
            assistant_fnc.get_car_details,
            assistant_fnc.create_car
        ]
    )
    # Create the session with OpenAI Realtime API
    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            voice="shimmer",
            temperature=0.8,
            modalities=["audio", "text"],
            instructions=INSTRUCTIONS
        )
    )
   # Start the session
    await session.start(agent=agent, room=ctx.room)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))