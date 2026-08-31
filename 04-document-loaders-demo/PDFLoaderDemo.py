#pip install pypdf
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\malah\Documents\Datasets\SamplePDFFile.pdf")

pages=loader.load_and_split()

print(type(pages))

print(pages[0])

print(pages[0].page_content)

print(pages[1].page_content)