from langchain.text_splitter import RecursiveCharacterTextSplitter

text = '''
Retrieval-Augmented Generation (RAG) is a technique for building LLM-powered applications. It leverages an external knowledge source to provide the LLM with relevant context and reduce hallucinations.
A naive RAG pipeline consists of a retrieval component (typically composed of an embedding model and a vector database) and a generative component (an LLM). At inference time, the user query is used to run a similarity search over the indexed documents to retrieve the most similar documents to the query and provide the LLM with additional context.

Typical RAG applications have two considerable limitations:
The naive RAG pipeline only considers one external knowledge source. However, some solutions might require two external knowledge sources, and some solutions might require external tools and APIs, such as web searches.
They are a one-shot solution, which means that context is retrieved once. There is no reasoning or validation over the quality of the retrieved context.

With the popularity of LLMs, new paradigms of AI agents and multi-agent systems have emerged. AI agents are LLMs with a role and task that have access to memory and external tools. The reasoning capabilities of LLMs help the agent plan the required steps and take action to complete the task at hand.
'''


spliter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
)

result = spliter.split_text(text)
print(len(result))
print(result)
