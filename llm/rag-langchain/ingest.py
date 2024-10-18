import os
import sys
import click
from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings

from langchain_text_splitters import MarkdownHeaderTextSplitter

headers = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4"),
]

splitter = MarkdownHeaderTextSplitter(headers)

@click.command()
@click.option('--vectorstore', default='vectorstore', help='Path to the vector store')
@click.option('--knowledge', default='knowledge', help='Path to the knowledge store')
def main(vectorstore, knowledge):

    if not os.path.isdir(knowledge):
        raise Exception(f'Knowledge base directory does not exist: {knowledge}')

    click.echo(f"Vector Store: {vectorstore}")
    click.echo(f"Knowledge Base: {knowledge}")

    files = Path(knowledge).glob("**/*.md")
    for filename in files:
        click.echo(f"- {filename}")
        with open(filename, encoding='utf-8') as f:
            splits = splitter.split_text(f.read())
            db = Chroma.from_documents(
                documents=splits,
                embedding=GPT4AllEmbeddings(),
                persist_directory=vectorstore)
            
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        click.echo(click.style(e, fg='red'))
        sys.exit(1)