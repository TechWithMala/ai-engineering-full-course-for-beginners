# 🔗 LangChain Chains — Hands-On Demos

This folder contains hands-on Python examples demonstrating **LangChain Chains** and how multiple steps can be connected to build practical LLM-powered applications.

These examples are part of the **AI Engineering Full Course for Beginners** by **Tech With Mala**.

## 🎥 Video Tutorial

Watch the complete tutorial on YouTube:

👉 **[LangChain Chains — Hands-On Tutorial](https://youtu.be/QPMqFh-kn3g)**

---

## 📚 What You'll Learn

In these demos, you'll learn how to:

* Create and use basic LangChain chains
* Connect prompts and LLMs together
* Build sequential workflows
* Route user queries to different chains
* Build RAG pipelines using chains
* Connect LLMs with SQL databases
* Create math-focused LLM chains
* Combine multiple chains to build more complex applications

---

## 📂 Demos Included

| File                                                             | Description                                               |
| ---------------------------------------------------------------- | --------------------------------------------------------- |
| [`SingleChainDemo.py`](./SingleChainDemo.py)                     | Demonstrates a basic LangChain chain                      |
| [`SimpleSequentialChainDemo.py`](./SimpleSequentialChainDemo.py) | Demonstrates a simple sequential chain                    |
| [`SequentialChainDemo.py`](./SequentialChainDemo.py)             | Demonstrates passing outputs between multiple chain steps |
| [`SequentialChainDemo - 2.py`](./SequentialChainDemo%20-%202.py) | Additional sequential chain example                       |
| [`RouterChainDemo.py`](./RouterChainDemo.py)                     | Demonstrates routing requests to different chains         |
| [`LLMRouterChainDemo.py`](./LLMRouterChainDemo.py)               | Demonstrates LLM-based routing between chains             |
| [`MathChainDemo.py`](./MathChainDemo.py)                         | Demonstrates a math-focused chain                         |
| [`MathChainDemo 2.py`](./MathChainDemo%202.py)                   | Additional math chain example                             |
| [`RAGChainDemo.py`](./RAGChainDemo.py)                           | Demonstrates a Retrieval-Augmented Generation chain       |
| [`SQLChainDemo.py`](./SQLChainDemo.py)                           | Demonstrates working with SQL data using an LLM           |

---

## 🧩 Chain Concepts Covered

### 1. Single Chain

A basic chain connects components together to process an input and produce an output.

```text
User Input
    ↓
Prompt
    ↓
LLM
    ↓
Response
```

### 2. Sequential Chains

Sequential chains allow multiple operations to run one after another.

```text
Input
  ↓
Chain 1
  ↓
Chain 2
  ↓
Chain 3
  ↓
Final Output
```

### 3. Router Chains

Router chains allow an application to determine which chain should handle a particular request.

```text
                ┌──→ Math Chain
                │
User Query → Router
                │
                ├──→ Science Chain
                │
                └──→ General Chain
```

### 4. RAG Chains

RAG chains combine retrieval with generation.

```text
User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
Prompt + Context
      ↓
LLM
      ↓
Answer
```

See [`RAGChainDemo.py`](./RAGChainDemo.py).

### 5. SQL Chains

SQL chains allow an LLM-powered application to translate natural-language questions into SQL queries and retrieve information from a database.

```text
"What are the top 5 customers?"
              ↓
             LLM
              ↓
        SQL Query
              ↓
          Database
              ↓
           Results
```

See [`SQLChainDemo.py`](./SQLChainDemo.py).

---

## ⚙️ Prerequisites

Make sure you have:

* Python 3.9+
* An OpenAI API key
* Basic Python knowledge
* Familiarity with LLM and LangChain fundamentals

Additional packages may be required depending on the demo.

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/TechWithMala/ai-engineering-full-course-for-beginners.git
```

Navigate to this folder:

```bash
cd ai-engineering-full-course-for-beginners/06-chains-demo
```

Install the required packages:

```bash
pip install langchain langchain-openai
```

Set your OpenAI API key.

### Windows

```bash
set OPENAI_API_KEY=your_api_key
```

### macOS / Linux

```bash
export OPENAI_API_KEY=your_api_key
```

Run a demo:

```bash
python SingleChainDemo.py
```

---

## 🔐 API Key Security

**Never hard-code your API key in your Python files.**

Use an environment variable instead:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

Make sure files containing API keys are included in `.gitignore`.

---

## 🎯 Recommended Learning Order

If you're new to LangChain Chains, follow the examples in this order:

1. `SingleChainDemo.py`
2. `SimpleSequentialChainDemo.py`
3. `SequentialChainDemo.py`
4. `SequentialChainDemo - 2.py`
5. `MathChainDemo.py`
6. `MathChainDemo 2.py`
7. `RouterChainDemo.py`
8. `LLMRouterChainDemo.py`
9. `RAGChainDemo.py`
10. `SQLChainDemo.py`

This progression moves from **basic chains → multi-step workflows → routing → RAG and SQL applications**.

---

## 📚 Related Course Repository

This folder is part of the **AI Engineering Full Course for Beginners** repository.

🔗 **GitHub:**
https://github.com/TechWithMala/ai-engineering-full-course-for-beginners

🎥 **YouTube:**
https://www.youtube.com/@TechWithMala

---

## ⭐ Support the Project

If these examples help you learn AI Engineering:

* ⭐ Star the repository
* 📺 Subscribe to the YouTube channel
* 💬 Share your feedback
* 🚀 Build something with the examples

Happy Learning! 🚀

