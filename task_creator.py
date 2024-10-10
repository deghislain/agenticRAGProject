from crewai import Task
import warnings

from tools import get_pdf_search_tool

warnings.filterwarnings('ignore')


def create_ai_question_answer_task(ai_expert, ai_doc):
    ai_question_answer = Task(
        description=(
             f"Utilize the semantic search tool on {ai_doc} "
             "to provide detailed and accurate answers to users' AI-related questions."
        ),
        expected_output="A clear, concise, and well-documented answer to users' questions",
        tools=[get_pdf_search_tool(ai_doc)],
        agent=ai_expert,
    )

    return ai_question_answer


def create_python_question_answer_task(py_expert, py_doc):
    python_question_answer = Task(
        description=(
            f"Utilize the semantic search tool on {py_doc} "
            "to provide detailed and code-rich answers to user's Python-related questions."
        ),
        expected_output="A clear, concise, and well-documented answer to users' questions, "
                        "including relevant code snippets and explanations.",
        tools=[get_pdf_search_tool(py_doc)],
        agent=py_expert,
    )

    return python_question_answer
