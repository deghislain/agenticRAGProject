from crewai import Agent
import warnings
from tools import get_pdf_search_tool
from langchain.agents import Tool

warnings.filterwarnings('ignore')


def get_ai_expert_agent(ai_document):
    ai_search_tool = get_pdf_search_tool(ai_document)

    tools = [
        Tool(
            name=f"Search {ai_document} content",
            description=F"A tool that can be used to semantic search a query from {ai_document}",
            func=ai_search_tool.run
        )
    ]
    ai_expert_agent = Agent(
        role="AI Expert",
        goal=f"Provide accurate information on AI-related topics using  using the tools at your disposal.",
        backstory=f"You're an AI expert with access to {ai_document}. Answer questions based on this document.",
        allow_delegation=False,
        tools=tools,
        verbose=True,
    )
    return ai_expert_agent


def get_python_expert_agent(python_document):
    py_search_tool = get_pdf_search_tool(python_document)

    tools = [
        Tool(
            name=f"Search {python_document} content",
            description=F"A tool that can be used to semantic search a query from {python_document}",
            func=py_search_tool.run
        )
    ]
    python_expert_agent = Agent(
        role="Python Developer Expert",
        goal=f"Assist with Python programming tasks using the tools at your disposal.",
        backstory=f"You're a Python developer expert with access to {python_document}."
                  f" Answer questions based on this document.",
        allow_delegation=False,
        tools=tools,
        verbose=True,
    )
    return python_expert_agent
