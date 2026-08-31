# pip install langchain
# pip install langchain-text-splitter

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter
)

# input document
sample_text = """
# Introduction to Machine Learning

Machine Learning (ML) is a subset of artificial intelligence that enables systems to learn and improve from experience. It focuses on developing computer programs that can access data and use it to learn for themselves.

## Types of Machine Learning

### Supervised Learning
Supervised learning is where the model is trained on a labeled dataset. The model learns to predict the output from the input data. Examples include:
- Classification
- Regression
- Neural Networks

### Unsupervised Learning
Unsupervised learning is where the model works on its own to discover patterns and information. Common examples include:
- Clustering
- Dimensionality Reduction
- Association

## Applications

Machine Learning has numerous real-world applications:
1. Image Recognition
2. Natural Language Processing
3. Recommendation Systems
4. Fraud Detection
"""

"""
    Splitting based on Markdown headers
"""
print("\n3. Markdown Header Text Splitter Example: Ideal for markdown documentation")

headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]

markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on
    )

docs = markdown_splitter.split_text(sample_text)
print(docs)

for i, doc in enumerate(docs, 1):
        print(f"\nDocument {i}:")
        print(f"Header: {doc.metadata.get('header_type', 'No header')}")
        print(f"Content:\n{doc.page_content}")
        print("-" * 50)