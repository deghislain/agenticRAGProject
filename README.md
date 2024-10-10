Agentic RAG Project

======================
Retrieval Augmented Generation for Efficient PDF Question Answering
The Agentic RAG Project is a cutting-edge application that leverages multiple agents to provide a seamless user 
experience when querying multiple PDF documents with diverse content.

Overview

This project utilizes a distributed architecture, assigning each agent ownership of a single PDF document. 
This approach enables faster question-answer sessions and reduces the number of tokens sent to the AI model, 
resulting in significant cost savings.

Key Features:
    -Multi-Agent Architecture: Efficiently handles multiple PDF documents
    -Faster Response Times: Optimized question-answer sessions
    -Cost-Effective: Reduced token usage minimizes AI model expenses


Technology Stack:
    *CrewAI
    *LLaMA
    *OLLaMA
    *Gemini
    *Embeddings
    *Streamlit


Getting Started
To run the Agentic RAG Project, follow these steps:
Prerequisites:
    Create a .streamlit/secrets.toml file with the required API keys:
    GROQ_API_KEY 
    GEMINI_API_KEY 


Run the Application:
    Install required dependencies
    Run streamlit run rag_agents_crew.py

     
