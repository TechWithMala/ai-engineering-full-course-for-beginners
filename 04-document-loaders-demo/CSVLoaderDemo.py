from langchain.document_loaders import CSVLoader

loader = CSVLoader(r"C:\Users\malah\Documents\Datasets\HR_Analytics.csv")

data=loader.load()

# print(data)

print(type(data))

# print(data[0])

print(data[1])
