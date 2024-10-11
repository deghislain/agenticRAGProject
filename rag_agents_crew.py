import streamlit as st
from crewai import Crew, Process
import agents_creator as agent
import task_creator as task
import os
import re

from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=os.environ['GROQ_API_KEY'],
    model_name="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=1000,
)

ai_expert_agent = None
ai_question_answer = None
python_expert_agent = None
python_question_answer = None

crew = None


def upload_documents():
    print("upload_documents START")
    label = "Upload multiple PDF document here"
    uploaded_files = st.file_uploader(label, type=['pdf'], accept_multiple_files=True, key=None, help=None,
                                      on_change=None,
                                      args=None, kwargs=None, disabled=False, label_visibility="visible")

    documents = []
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        documents.append(file_name)
        with open(file_name + ".pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
    print("upload_documents END")
    return documents


def create_crew(ai_expert_agent, ai_question_answer, python_expert_agent, python_question_answer):
    print("create_crew START")
    crew = Crew(
        agents=[ai_expert_agent, python_expert_agent],
        tasks=[ai_question_answer, python_question_answer],

        manager_llm=llm,
        process=Process.hierarchical,
        verbose=True,
        memory=True
    )
    print("create_crew END")
    return crew


def main():
    global crew, ai_expert_agent, ai_question_answer, python_expert_agent, python_question_answer
    docs = upload_documents()

    for doc in docs:
        if re.search("Coding In Python", doc):
            python_expert_agent = agent.get_python_expert_agent(doc)
            python_question_answer = task.create_python_question_answer_task(python_expert_agent, doc)
            print("python_expert_agent created")
        elif re.search("compact-guide-to-large-language-models", doc):
            ai_expert_agent = agent.get_ai_expert_agent(doc)
            ai_question_answer = task.create_ai_question_answer_task(ai_expert_agent, doc)
            print("ai_expert_agent created")


if __name__ == "__main__":
    main()
    question = st.chat_input("Type your question here:")
    if question:
        user_question = {
            'question': question
        }
        if ai_expert_agent and ai_question_answer and python_expert_agent and python_question_answer:
            crew = create_crew(ai_expert_agent, ai_question_answer, python_expert_agent, python_question_answer)
            response = crew.kickoff(inputs=user_question)
            st.write(response)
            print(response)
