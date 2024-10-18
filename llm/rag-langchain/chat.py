import os
import sys
import click

from langchain_chroma import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings

from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA

@click.command()
@click.option('--vectorstore', default='vectorstore', help='Path to the vector store')
def main(vectorstore):

    if not os.path.isdir(vectorstore):
        raise Exception(f'Vector store directory does not exist: {vectorstore}')
    
    click.echo(f"Vector Store: {vectorstore}")

    vectorstore = Chroma(embedding_function=GPT4AllEmbeddings(), persist_directory=vectorstore)

    template = """You are a helpful assistant that answers questions of a person learning about a topic.
    Use the context to answer the question.
    If you don't know the answer, say that you don't know, do not make up facts.
    Keep the answer concise.
    {context}
    Question: {question}
    Helpful Answer:"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )

    llm = OllamaLLM(model="llama3.1", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt},
    )

    while True:
        query = input("\nQuery: ")

        if query == "exit":
            break

        if query.strip() == "":
            continue

        result = qa_chain.invoke({"query": query})

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        click.echo(click.style(e, fg='red'))
        sys.exit(1)