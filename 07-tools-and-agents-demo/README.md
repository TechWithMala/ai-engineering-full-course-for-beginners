# 🛠️ Tools & AI Agents — Hands-On Demos

This folder contains hands-on Python examples demonstrating **LLM tools, tool calling, AI agents, and multi-agent workflows**.

These examples are part of the **AI Engineering Full Course for Beginners** by **Tech With Mala**.

## 🎥 Video Tutorial

Watch the complete tutorial on YouTube:

👉 **[Tools & AI Agents — Hands-On Tutorial](https://youtu.be/QPMqFh-kn3g)**

---

## 📚 What You'll Learn

In these demos, you'll learn how AI agents can go beyond generating text by **using tools to interact with external systems and perform real-world tasks**.

You'll learn how to:

* Understand what tools are in AI applications
* Give LLMs access to external tools
* Build tool-calling workflows
* Create AI agents that decide which tools to use
* Build agents that work with mathematical tools
* Connect agents to SQL databases
* Perform web scraping with AI-powered workflows
* Build multi-agent applications with CrewAI
* Create agents for practical business use cases

---

## 🧠 Tools vs. AI Agents

A **tool** gives an LLM access to a specific capability.

Examples include:

* Calculator
* Web search
* Web scraper
* SQL database
* API
* Python function

An **AI agent** can decide **which tool to use, when to use it, and how to combine tools to accomplish a task**.

### Typical Agent Workflow

```text
User Request
     ↓
     LLM
     ↓
Decide What To Do
     ↓
Select Tool
     ↓
Execute Tool
     ↓
Observe Result
     ↓
LLM
     ↓
Final Answer
```

This ability to reason about actions and use external tools is a key concept in modern AI agent systems.

---

## 📂 Demos Included

| File                                                                                             | Description                                            |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| [`MathTools_Agents_Usecase.py`](./MathTools_Agents_Usecase.py)                                   | Demonstrates an AI agent using mathematical tools      |
| [`SQLDatabaseTool_SqlAgent.py`](./SQLDatabaseTool_SqlAgent.py)                                   | Demonstrates an agent interacting with a SQL database  |
| [`WebScraping_Using_Apify.py`](./WebScraping_Using_Apify.py)                                     | Demonstrates web scraping using Apify                  |
| [`CrewAI_Usecase1_WebScraping.py`](./CrewAI_Usecase1_WebScraping.py)                             | CrewAI-based web scraping use case                     |
| [`CrewAI_Usecase2_Personalized_Email_Drafts.py`](./CrewAI_Usecase2_Personalized_Email_Drafts.py) | Uses CrewAI agents to create personalized email drafts |
| [`CrewAI_Usecase3_Trading_Platform.py`](./CrewAI_Usecase3_Trading_Platform.py)                   | Demonstrates a multi-agent trading platform use case   |

---

## 🔢 1. Math Tools & Agents

[`MathTools_Agents_Usecase.py`](./MathTools_Agents_Usecase.py)

This example demonstrates how an AI agent can use a mathematical tool instead of relying entirely on the LLM to perform calculations.

```text
User Question
      ↓
    Agent
      ↓
Math Tool
      ↓
Calculation
      ↓
Agent
      ↓
Final Answer
```

This illustrates an important agent concept:

> **The LLM decides when a tool is needed, while the tool performs the actual operation.**

---

## 🗄️ 2. SQL Database Tool & SQL Agent

[`SQLDatabaseTool_SqlAgent.py`](./SQLDatabaseTool_SqlAgent.py)

This example demonstrates how an AI agent can interact with a SQL database.

A user can ask questions using natural language, while the agent determines how to query the database.

```text
Natural Language Question
          ↓
        Agent
          ↓
      SQL Tool
          ↓
      Database
          ↓
       Results
          ↓
        Agent
          ↓
     Final Answer
```

This pattern is useful for building **natural-language database interfaces**.

---

## 🌐 3. Web Scraping with Apify

[`WebScraping_Using_Apify.py`](./WebScraping_Using_Apify.py)

This example demonstrates using **Apify** for web scraping.

Web scraping tools can give AI applications access to information available on websites.

```text
Website
   ↓
Apify
   ↓
Scraped Data
   ↓
AI Application
   ↓
Useful Information
```

This is a practical example of connecting an AI application with an external service.

---

# 🤖 CrewAI Use Cases

The final examples demonstrate **CrewAI**, a framework for building applications where multiple specialized AI agents collaborate.

Instead of asking one agent to perform every task, we can divide a complex workflow among multiple agents.

```text
                 ┌──→ Research Agent
                 │
User Request ────┼──→ Analysis Agent
                 │
                 └──→ Writing Agent
                         ↓
                    Final Result
```

Each agent can have a specific **role, goal, tools, and responsibilities**.

---

## 🌐 4. CrewAI Web Scraping

[`CrewAI_Usecase1_WebScraping.py`](./CrewAI_Usecase1_WebScraping.py)

This example demonstrates a multi-agent workflow for a web-scraping-related task.

It shows how different agents can collaborate to complete a larger workflow.

---

## ✉️ 5. CrewAI Personalized Email Drafts

[`CrewAI_Usecase2_Personalized_Email_Drafts.py`](./CrewAI_Usecase2_Personalized_Email_Drafts.py)

This example demonstrates using multiple agents to create **personalized email drafts**.

A multi-agent workflow can divide responsibilities such as:

```text
Research
   ↓
Analyze Information
   ↓
Personalize Content
   ↓
Draft Email
```

This demonstrates how agent collaboration can be used for practical business workflows.

---

## 📈 6. CrewAI Trading Platform

[`CrewAI_Usecase3_Trading_Platform.py`](./CrewAI_Usecase3_Trading_Platform.py)

This example demonstrates a more advanced **multi-agent application** based on a trading-platform use case.

Different agents can specialize in different responsibilities within the overall workflow.

> ⚠️ This is an educational AI-agent demonstration and should not be treated as financial advice or used as an autonomous trading system without appropriate validation, risk controls, and human oversight.

---

# 🏗️ Agent Architecture

The examples in this folder demonstrate the evolution from simple tools to more sophisticated agent systems:

```text
Tools
  ↓
Tool Calling
  ↓
Single AI Agent
  ↓
Agent + External Systems
  ↓
Multiple Specialized Agents
  ↓
Multi-Agent System
```

Understanding this progression is important when learning **AI Engineering and Agentic AI**.

---

## ⚙️ Prerequisites

Depending on the example, you may need:

* Python 3.9+
* OpenAI API key
* LangChain
* CrewAI
* Apify account/API key
* SQL database or sample database
* Basic Python knowledge
* Basic understanding of LLMs

Individual demos may require additional dependencies.

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/TechWithMala/ai-engineering-full-course-for-beginners.git
```

Navigate to this folder:

```bash
cd ai-engineering-full-course-for-beginners/07-tools-and-agents-demo
```

Install the packages required by the specific example you want to run.

For example:

```bash
pip install langchain langchain-openai
```

For CrewAI examples:

```bash
pip install crewai
```

For Apify-based examples:

```bash
pip install apify-client
```

---

## 🔐 API Key Security

Never hard-code API keys or other secrets directly in your Python files.

Avoid:

```python
api_key = "your-secret-api-key"
```

Instead, use environment variables:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

For Apify:

```python
apify_token = os.getenv("APIFY_API_TOKEN")
```

Make sure your `.env` files and other files containing secrets are included in `.gitignore`.

---

## 🎯 Recommended Learning Order

If you're new to AI agents, follow these examples in order:

1. `MathTools_Agents_Usecase.py`
2. `SQLDatabaseTool_SqlAgent.py`
3. `WebScraping_Using_Apify.py`
4. `CrewAI_Usecase1_WebScraping.py`
5. `CrewAI_Usecase2_Personalized_Email_Drafts.py`
6. `CrewAI_Usecase3_Trading_Platform.py`

This progression takes you from **basic tool usage → agents → external systems → multi-agent applications**.

---

## 📌 Key Takeaways

After completing these examples, you should understand:

* What an AI tool is
* Why LLMs need tools to interact with external systems
* How tool calling works conceptually
* How AI agents select and use tools
* How agents can work with databases
* How AI applications can interact with websites
* How CrewAI enables multi-agent workflows
* How specialized agents can collaborate on complex tasks

---

## 📚 Course Repository

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
* 🚀 Build your own AI agent

Happy Learning! 🤖🚀

