#pip install beautifulsoup4
#pip install -U lxml

from langchain.document_loaders import BSHTMLLoader

loader=BSHTMLLoader(r"C:\Users\malah\Documents\Datasets\Test1.html")

data=loader.load()

print(data)