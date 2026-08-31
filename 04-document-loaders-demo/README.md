# Document Loaders Demo

This folder contains hands-on Python examples demonstrating how to load and process different types of documents using LangChain document loaders.

Document loaders are an important part of AI and RAG applications because they allow applications to read data from different sources and convert it into a format that can be processed, chunked, embedded, and retrieved.

## Document Loaders Covered

### 1. PDF Loader

Demonstrates how to load and extract text from PDF documents using LangChain.

📄 [`PDFLoaderDemo.py`](./PDFLoaderDemo.py)

### 2. CSV Loader

Demonstrates how to load structured data from CSV files and convert the rows into documents that can be processed by an LLM or RAG pipeline.

📄 [`CSVLoaderDemo.py`](./CSVLoaderDemo.py)

### 3. HTML Loader

Demonstrates how to load and extract content from HTML documents.

📄 [`HTMLLoaderDemo.py`](./HTMLLoaderDemo.py)

## Why Document Loaders Matter

Real-world AI applications often need to work with information stored in different formats.

Document loaders help you:

* Load data from different file formats
* Extract text and structured information
* Convert external data into LangChain documents
* Prepare data for text chunking
* Prepare documents for embeddings and vector databases
* Build RAG and other LLM-powered applications

## Typical Document Processing Pipeline

A common workflow for RAG applications is:

```text
Documents
    ↓
Document Loader
    ↓
Text Splitting / Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retrieval
    ↓
LLM
    ↓
Answer
```

## Course Video

🎥 Watch the complete **AI Engineering Full Course for Beginners** on YouTube:

[AI Engineering Full Course for Beginners](https://youtu.be/QPMqFh-kn3g)

## Course Repository

💻 Find all the code and examples for this course in the GitHub repository:

[AI Engineering Full Course for Beginners](https://github.com/TechWithMala/ai-engineering-full-course-for-beginners)

## About This Course

This course provides a hands-on introduction to AI Engineering, covering LLMs, Generative AI, RAG, LangChain, AI Agents, embeddings, vector databases, and more.

The code in this repository is provided as a companion to the YouTube course.

