import os
import sys
import click

from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain_community.embeddings import GPT4AllEmbeddings

docs = [
    Document(page_content="Barbajorgos was the first man on the Venus"),
    Document(page_content="Franek was on the Moon"),
    Document(page_content="Zosia likes pizza"),
    Document(page_content="Ania likes chips"),
]

@click.command()
@click.option('--vectorstore', default='vectorstore', help='Path to the vector store')
@click.option('--knowledge', default='knowledge', help='Path to the knowledge store')
def main(vectorstore, knowledge):

    click.echo(f"Vector Store: {vectorstore}")
    click.echo(f"Knowledge Base: {knowledge}")

    db = Chroma.from_documents(
        documents=docs,
        embedding=GPT4AllEmbeddings(),
        persist_directory=vectorstore)
    
    # raise Exception("Not implemented")
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        click.echo(click.style(e, fg='red'))
        sys.exit(1)