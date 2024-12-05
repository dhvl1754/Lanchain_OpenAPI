#pip install openai
#pip install langchain
#pip install langchain-openai
#pip install pypdf
#pip install langchain-community
#pip install langchainhub
#pip install faiss-cpu
#pip install python-dotenv

from langchain_community.document_loaders import PyPDFLoader

loaders = [
    PyPDFLoader("../Data/botanical.pdf"),
    PyPDFLoader("../Data/astronomical.pdf"),
    PyPDFLoader("../Data/biological.pdf"),
    PyPDFLoader("../Data/cosmological.pdf"),
    PyPDFLoader("../Data/culinary.pdf"),
    PyPDFLoader("../Data/pharmaceutical.pdf")
]

docs = []