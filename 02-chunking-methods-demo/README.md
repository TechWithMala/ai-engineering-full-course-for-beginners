# Chunking Methods Demo

This folder contains hands-on Python examples demonstrating different text chunking methods used in Retrieval-Augmented Generation (RAG) and AI applications.

Text chunking is an important step in a RAG pipeline because large documents need to be divided into smaller, meaningful pieces before they can be embedded and stored in a vector database.

## Chunking Methods Covered

### 1. Character Text Splitter

Demonstrates how to split text based on a fixed number of characters.

📄 [`CharacterTextSplitterDemo.py`](./CharacterTextSplitterDemo.py)

### 2. Recursive Character Text Splitter

Demonstrates recursive text splitting using a hierarchy of separators to create more meaningful chunks while maintaining context.

📄 [`RecursiveCharacterTextSplitterDemo.py`](./RecursiveCharacterTextSplitterDemo.py)

### 3. Token Text Splitter

Demonstrates splitting text based on tokens rather than characters.

📄 [`TokenTextSplitterDemo.py`](./TokenTextSplitterDemo.py)

### 4. Markdown Header Text Splitter

Demonstrates how Markdown documents can be split based on their header structure, helping preserve the document's organization and context.

📄 [`MarkdownHeaderTextSplitterDemo.py`](./MarkdownHeaderTextSplitterDemo.py)

## Why Chunking Matters in RAG

In a RAG system, documents are typically too large to send directly to an LLM or embed as a single piece of text.

Chunking helps:

* Break large documents into manageable pieces
* Improve retrieval accuracy
* Preserve relevant context
* Create useful embeddings
* Reduce unnecessary information during retrieval

Different chunking strategies work better for different types of documents and use cases.

## Course Video

🎥 Watch the complete **AI Engineering Full Course for Beginners** on YouTube:

[AI Engineering Full Course for Beginners](https://youtu.be/QPMqFh-kn3g)

## Course Repository

💻 Find all the code and examples for this course in the GitHub repository:

[AI Engineering Full Course for Beginners](https://github.com/TechWithMala/ai-engineering-full-course-for-beginners)

## About This Course

This course provides a hands-on introduction to AI Engineering, covering LLMs, Generative AI, RAG, LangChain, AI Agents, embeddings, vector databases, and more.

The code in this repository is provided as a companion to the YouTube course.

