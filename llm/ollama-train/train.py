from langchain.llms import Ollama
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

# make sure that model is available: ollama pull llama2
ollama = Ollama(base_url='http://localhost:11434', model="llama2")
oembed = OllamaEmbeddings(base_url="http://localhost:11434", model="llama2")

# print(ollama("why is the sky blue"))

loader = WebBaseLoader("https://www.gutenberg.org/files/1727/1727-0.txt")
data = loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
all_splits = text_splitter.split_documents(data)
vectorstore = Chroma.from_documents(documents=all_splits, embedding=oembed)

question="Who is Neleus and who is in Neleus' family?"

docs = vectorstore.similarity_search(question)
len(docs)