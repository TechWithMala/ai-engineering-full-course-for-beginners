# 🧠 LangChain Memory Demo

This module demonstrates how **memory works in LangChain** and how conversational AI applications can maintain context across multiple interactions.

You'll explore different memory strategies and understand when to use each one.

---

## 🎥 Video Tutorial

Follow the corresponding lesson on the **Tech With Mala YouTube channel**:

👉 [**Watch the AI Engineering Full Course**](https://www.youtube.com/watch?v=QPMqFh-kn3g)

The examples in this folder are designed to be used alongside the video lesson.

---

## 📚 Examples in This Module

### 1. Conversation Buffer Memory

📄 [`ConversationBufferMemoryDemo.py`](./ConversationBufferMemoryDemo.py)

Demonstrates how conversation history can be stored and passed to the language model.

**Key concepts:**

* Conversation history
* Maintaining context
* User and AI messages
* Basic conversational memory

---

### 2. Conversation Buffer Window Memory

📄 [`ConversationBufferWindowMemoryDemo.py`](./ConversationBufferWindowMemoryDemo.py)

Demonstrates how to maintain only a limited number of recent conversation messages.

**Key concepts:**

* Window-based memory
* Limiting conversation history
* Reducing token usage
* Maintaining recent context

This approach can be useful when the complete conversation history becomes too large.

---

### 3. Conversation Summary Memory

📄 [`ConversationSummaryMemoryDemo.py`](./ConversationSummaryMemoryDemo.py)

Demonstrates how conversation history can be summarized instead of storing every message.

**Key concepts:**

* Conversation summarization
* Managing long conversations
* Reducing context size
* Maintaining important information

---

## 🧩 Memory Strategies

| Memory Type                           | How It Works                             | Best For                           |
| ------------------------------------- | ---------------------------------------- | ---------------------------------- |
| **Conversation Buffer Memory**        | Stores the complete conversation history | Short conversations                |
| **Conversation Buffer Window Memory** | Keeps only the most recent messages      | Conversations with limited context |
| **Conversation Summary Memory**       | Summarizes previous conversation history | Longer conversations               |

---

## 🔄 How Conversation Memory Works

A typical conversational application follows this flow:

```text
User Message
     ↓
Retrieve Conversation Memory
     ↓
Add Previous Context
     ↓
Send Context + New Message to LLM
     ↓
Generate Response
     ↓
Update Conversation Memory
```

Without memory, an LLM generally processes each request independently.

With memory, the application can provide relevant previous conversation context to the model.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/TechWithMala/ai-engineering-full-course-for-beginners.git
```

Navigate to the project:

```bash
cd ai-engineering-full-course-for-beginners
```

---

### 2. Create and Activate a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

Depending on the example and LangChain version, you may need:

```bash
pip install langchain langchain-openai
```

---

## 🔐 API Key

Some examples require an OpenAI API key.

Set your API key as an environment variable rather than placing it directly in your source code.

### Windows

```bash
set OPENAI_API_KEY=your_api_key_here
```

### macOS / Linux

```bash
export OPENAI_API_KEY=your_api_key_here
```

Or use a `.env` file and load the environment variable in your application.

**Never commit API keys or other secrets to GitHub.**

---

## ▶️ Running the Examples

From the `05-memory-demo` directory, run an example with:

```bash
python ConversationBufferMemoryDemo.py
```

Or:

```bash
python ConversationBufferWindowMemoryDemo.py
```

Or:

```bash
python ConversationSummaryMemoryDemo.py
```

---

## 🎯 What You'll Learn

After completing this module, you should understand:

* What conversational memory is
* Why memory is important for AI applications
* How conversation history is maintained
* How buffer memory works
* How window memory works
* How summary memory works
* The trade-offs between different memory approaches
* How memory affects context and token usage

---

## 💡 Experiment

Try modifying the examples to understand how different memory strategies behave.

For example:

* Ask multiple questions in the same conversation.
* Increase or decrease the window size.
* Compare full conversation history with summarized history.
* Start a new conversation and observe what context is retained.
* Experiment with longer conversations.

The goal is not just to run the code, but to understand **how memory changes the behavior of an AI application**.

---

## 📂 Folder Structure

```text
05-memory-demo/
│
├── ConversationBufferMemoryDemo.py
├── ConversationBufferWindowMemoryDemo.py
├── ConversationSummaryMemoryDemo.py
└── README.md
```

---

## 📌 Important Note

LangChain evolves quickly, and some memory APIs may change between versions.

If an example doesn't work with your installed version of LangChain, check the current LangChain documentation and adjust the imports or APIs accordingly.

The examples are provided primarily for **learning and demonstration purposes**.

---

## 📺 Tech With Mala

Learn more about AI Engineering, Generative AI, LLMs, RAG, LangChain, AI Agents, Multi-Agent Systems, and related technologies.

👉 **YouTube:** https://www.youtube.com/@TechWithMala

---

**Happy Learning! 🧠🤖🚀**
