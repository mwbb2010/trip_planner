# agent_models.py

from pydantic import BaseModel

class Agent(BaseModel):
    role: str
    goal: str
    backstory: str
    tools: list
    llm: ChatOpenAI  # Assuming ChatOpenAI is a Pydantic model
    verbose: bool