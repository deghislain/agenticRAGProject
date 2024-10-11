from crewai import Task
import warnings

from tools import get_pdf_search_tool
from langchain.agents import Tool

warnings.filterwarnings('ignore')


def create_ai_question_answer_task(ai_expert, ai_doc):
    ai_question_answer = Task(
        description=(
             f"Search and provide detailed answers to user's AI-related questions using {ai_doc}."
        ),
        expected_output="A clear, concise, and well-documented answer to users' AI-related questions",
        agent=ai_expert,
    )

    return ai_question_answer


def create_python_question_answer_task(py_expert, py_doc):
    python_question_answer = Task(
        description=(
            f"Search and provide detailed and code-rich answers to user's Python-related questions using {py_doc}."
        ),
        expected_output="A clear, concise, and well-documented answer to users' questions, "
                        "including relevant code snippets and explanations.",
        agent=py_expert,
    )

    return python_question_answer
