# pip install langchain
# pip install langchain-text-splitter

from langchain_text_splitters import (
    CharacterTextSplitter
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
Basic character-based text splitting
"""
print("\n1. Character Text Splitter Example: Best for simple text splitting")

splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=200,
        chunk_overlap=50
    )
chunks = splitter.split_text(sample_text)
print(chunks)
print(type(chunks))

for i, chunk in enumerate(chunks, 1):
        print(f"\nChunk {i}:")
        print(chunk)
        print("-" * 50)