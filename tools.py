from crewai_tools import PDFSearchTool


def get_pdf_search_tool(path):
    path = path + ".pdf"
    return PDFSearchTool(
        pdf=path,
        config=dict(
            llm=dict(
                provider="google",  # or google, openai, anthropic, llama2, ...
                config=dict(
                    model="gemini",
                    temperature=0.0,
                    # top_p=1,
                    # stream=true,
                ),
            ),
            embedder=dict(
                provider="google",  # or openai, ollama, ...
                config=dict(
                    model="models/embedding-001",
                    task_type="retrieval_document",
                    # title="Embeddings",
                ),
            ),
        )
    )
