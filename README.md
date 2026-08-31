# 🚀 AI Engineering Full Course for Beginners

A complete hands-on **AI Engineering course for beginners** covering LLMs, Generative AI, RAG, LangChain, AI Agents, embeddings, vector databases, Hugging Face, and more.

This repository contains the **companion code and examples** for the AI Engineering Full Course by **Tech With Mala**.

---

## 🎥 Course on YouTube

Follow the complete course on YouTube:

👉 **[Tech With Mala — YouTube Channel](https://www.youtube.com/watch?v=QPMqFh-kn3g)**

The repository is designed to be used alongside the video lessons, so you can follow the concepts and run the examples yourself.

---

# 📚 Course Modules

The course is organized into progressive modules, starting with the fundamentals and gradually moving toward more advanced AI Engineering concepts.

| Module                                                        | Topic                  | Description                                                         |
| ------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------- |
| 📁 [01-rag-demo](./01-rag-demo)                               | **RAG**                | Build Retrieval-Augmented Generation applications                   |
| 📁 [02-chunking-methods-demo](./02-chunking-methods-demo)     | **Text Chunking**      | Explore different document chunking strategies                      |
| 📁 [03-prompt-engineering-demo](./03-prompt-engineering-demo) | **Prompt Engineering** | Learn practical prompt engineering techniques                       |
| 📁 [04-document-loaders-demo](./04-document-loaders-demo)     | **Document Loaders**   | Load and process different document formats                         |
| 📁 [05-memory-demo](./05-memory-demo)                         | **Memory**             | Build conversational applications with memory                       |
| 📁 [06-chains-demo](./06-chains-demo)                         | **LangChain Chains**   | Build single, sequential, router, RAG, and SQL chains               |
| 📁 [07-tools-and-agents-demo](./07-tools-and-agents-demo)     | **Tools & AI Agents**  | Build tool-using agents and multi-agent workflows                   |
| 📁 [08-huggingface-demo](./08-huggingface-demo)               | **Hugging Face**       | Work with embeddings, summarization, translation, and vision models |

---

# 🧭 Learning Path

If you're completely new to AI Engineering, follow the modules in order:

```text
LLM Fundamentals
       ↓
Prompt Engineering
       ↓
Document Processing
       ↓
Embeddings
       ↓
RAG
       ↓
Memory
       ↓
LangChain Chains
       ↓
Tools
       ↓
AI Agents
       ↓
Multi-Agent Systems
       ↓
Hugging Face
       ↓
Advanced AI Engineering
```

The goal is to build your understanding progressively rather than jumping directly into complex agent systems.

---

# 🧠 What You'll Learn

Throughout the course, you'll work with concepts including:

### Generative AI

* Large Language Models (LLMs)
* Generative AI concepts
* Prompt engineering
* LLM applications

### RAG

* Retrieval-Augmented Generation
* Document processing
* Text chunking
* Embeddings
* Vector search
* Retrieval
* Context-aware generation

### LangChain

* Prompts
* Chains
* Sequential chains
* Router chains
* RAG chains
* SQL chains
* Memory
* Tools
* Agents

### AI Agents

* Tool calling
* Agent workflows
* External tools
* SQL agents
* Web scraping
* Agent decision-making
* Multi-agent systems
* CrewAI

### Hugging Face

* Pre-trained models
* Sentence embeddings
* Text summarization
* Translation
* Image understanding
* Multimodal AI

---

# 🛠️ Technologies & Frameworks

The course uses a variety of tools and frameworks from the modern AI Engineering ecosystem, including:

* 🐍 Python
* 🦜 LangChain
* 🤗 Hugging Face
* 🤖 OpenAI
* 👥 CrewAI
* 🗄️ Vector databases
* 🔎 FAISS
* 🌐 Apify
* 🗃️ SQL databases

The technologies used may evolve as the course is updated.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/TechWithMala/ai-engineering-full-course-for-beginners.git
```

Navigate into the repository:

```bash
cd ai-engineering-full-course-for-beginners
```

---

## 2. Create a Virtual Environment

Creating a virtual environment is recommended.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

Dependencies may vary by module.

Each module's README provides instructions for the examples contained in that folder.

For example:

```bash
pip install langchain langchain-openai
```

For Hugging Face examples:

```bash
pip install transformers sentence-transformers torch
```

For CrewAI examples:

```bash
pip install crewai
```

---

# 🔐 API Keys & Security

Several examples require API keys.

**Never commit API keys, passwords, tokens, or other secrets to GitHub.**

Use environment variables instead.

For example:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

For Apify:

```python
import os

apify_token = os.getenv("APIFY_API_TOKEN")
```

Make sure `.env` files and other files containing secrets are included in `.gitignore`.

---

# 📂 Repository Structure

```text
ai-engineering-full-course-for-beginners/
│
├── 01-rag-demo/
├── 02-chunking-methods-demo/
├── 03-prompt-engineering-demo/
├── 04-document-loaders-demo/
├── 05-memory-demo/
├── 06-chains-demo/
├── 07-tools-and-agents-demo/
├── 08-huggingface-demo/
│
├── .gitignore
└── README.md
```

Each module contains its own `README.md` with an overview of the examples and instructions for getting started.

---

# 🎯 Who Is This Course For?

This course is designed for learners who want to understand **how to build AI-powered applications**, not just use AI tools.

It's suitable for:

* Python developers
* Software developers
* Data scientists
* ML engineers
* AI/ML beginners
* Students learning Generative AI
* Developers transitioning into AI Engineering

Basic Python knowledge is recommended.

---

# 💡 How to Use This Repository

The best way to use this repository is:

```text
Watch the Lesson
      ↓
Understand the Concept
      ↓
Open the Corresponding Folder
      ↓
Read the README
      ↓
Run the Example
      ↓
Experiment & Modify
      ↓
Build Your Own Application
```

Don't just copy and run the code. Try changing the prompts, models, inputs, and workflows to understand how the application behaves.

---

# 📺 Tech With Mala

Follow **Tech With Mala** for practical tutorials covering:

* AI Engineering
* Generative AI
* LLMs
* RAG
* LangChain
* LangGraph
* AI Agents
* Multi-Agent Systems
* CrewAI
* Hugging Face
* Vector Databases
* Production AI Applications

### YouTube

👉 https://www.youtube.com/@TechWithMala

---

# ⭐ Support the Repository

If you find this repository useful:

⭐ **Star the repository**

📺 **Subscribe to the YouTube channel**

💬 **Share your feedback**

🚀 **Build something with the examples**

---

## 📌 Disclaimer

The examples in this repository are provided for **educational purposes**.

AI frameworks, APIs, libraries, and model providers evolve quickly. Some examples may require updates to dependencies or API usage over time.

Always review the documentation of the underlying libraries and services when running the examples.

---

## 🚀 Keep Learning

AI Engineering is a rapidly evolving field.

Start with the fundamentals, build projects, experiment with different models and frameworks, and gradually move toward production-grade AI systems.

**Happy Learning! 🤖🚀**
