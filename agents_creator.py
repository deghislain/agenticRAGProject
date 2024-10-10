from crewai import Agent
import warnings
from tools import get_pdf_search_tool

warnings.filterwarnings('ignore')


def get_ai_expert_agent(ai_document):
    ai_expert_agent = Agent(
        role="AI Knowledge Consultant",
        goal=f"Provide accurate information on AI-related topics using  using the tools at your disposal.",
        backstory=f"You're an AI expert with access to {ai_document}. Answer questions based on this document.",
        allow_delegation=False,
        verbose=True,
    )
    return ai_expert_agent


def get_python_expert_agent(python_document):
    python_expert_agent = Agent(
        role="Python Programming Specialist",
        goal=f"Assist with Python programming tasks using the tools at your disposal.",
        backstory=f"You're a Python developer with access to {python_document}. Answer questions based on this document.",
        allow_delegation=False,
        verbose=True,
    )
    return python_expert_agent
