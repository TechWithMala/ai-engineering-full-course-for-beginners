# 🤗 Hugging Face — Hands-On Demos

This folder contains hands-on Python examples demonstrating how to use **Hugging Face models** for common NLP, Generative AI, and multimodal AI tasks.

These examples are part of the **AI Engineering Full Course for Beginners** by **Tech With Mala**.

## 🎥 Video Tutorial

Watch the complete tutorial on YouTube:

👉 **[Hugging Face — Hands-On Tutorial](https://youtu.be/QPMqFh-kn3g)**

---

## 📚 What You'll Learn

In these demos, you'll learn how to use Hugging Face models for:

* Sentence embeddings
* Text summarization
* Language translation
* Image understanding
* Working with pre-trained Transformer models
* Using Hugging Face models in Python
* Building AI applications using open-source models

---

## 📂 Demos Included

| File                                                         | Description                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------- |
| [`SentenceEmbeddings.py`](./SentenceEmbeddings.py)           | Generate sentence embeddings using a Hugging Face model       |
| [`SentenceSummarization.py`](./SentenceSummarization.py)     | Summarize text using a pre-trained Hugging Face model         |
| [`SentenceSummarization-2.py`](./SentenceSummarization-2.py) | Additional text summarization example                         |
| [`SentenceTranslation.py`](./SentenceTranslation.py)         | Translate text using a pre-trained Hugging Face model         |
| [`ImageUnderstanding.py`](./ImageUnderstanding.py)           | Demonstrate image understanding using a vision-language model |

---

## 🧠 What is Hugging Face?

**Hugging Face** provides an ecosystem of open-source AI models, datasets, and tools for building machine learning and Generative AI applications.

The Hugging Face Hub provides models for tasks such as:

* 📝 Text generation
* 🔤 Text classification
* 🧩 Embeddings
* 📄 Summarization
* 🌍 Translation
* 👁️ Image understanding
* 🎤 Speech
* 🤖 Multimodal AI

Instead of training every model from scratch, developers can use **pre-trained models** and integrate them into their applications.

---

## 🔢 1. Sentence Embeddings

[`SentenceEmbeddings.py`](./SentenceEmbeddings.py)

Embeddings convert text into numerical vectors that represent semantic meaning.

```text
Text
 ↓
Embedding Model
 ↓
Vector Representation
```

Embeddings are commonly used for:

* Semantic search
* RAG
* Document similarity
* Recommendation systems
* Clustering
* Duplicate detection

---

## 📝 2. Text Summarization

[`SentenceSummarization.py`](./SentenceSummarization.py)

This example demonstrates how a pre-trained Hugging Face model can generate a shorter summary from a longer piece of text.

```text
Long Text
    ↓
Hugging Face Model
    ↓
Summary
```

Summarization can be useful for:

* Documents
* News articles
* Research papers
* Meeting notes
* Customer feedback
* Long-form content

---

## 📝 3. Additional Summarization Example

[`SentenceSummarization-2.py`](./SentenceSummarization-2.py)

This file provides another hands-on example of text summarization using a Hugging Face model.

---

## 🌍 4. Sentence Translation

[`SentenceTranslation.py`](./SentenceTranslation.py)

This example demonstrates machine translation using a pre-trained Hugging Face model.

```text
Source Text
     ↓
Translation Model
     ↓
Translated Text
```

Translation models can be used to build multilingual AI applications.

---

## 🖼️ 5. Image Understanding

[`ImageUnderstanding.py`](./ImageUnderstanding.py)

This example demonstrates how Hugging Face vision-language models can process and understand images.

```text
Image
  ↓
Vision-Language Model
  ↓
Generated Understanding
```

This introduces the concept of **multimodal AI**, where models can work with more than one type of input, such as images and text.

---

## 🏗️ Hugging Face in AI Engineering

Hugging Face models can serve as building blocks for larger AI applications.

```text
                Hugging Face
                     ↓
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
  Embeddings    Summarization  Translation
       ↓             ↓             ↓
      RAG        Documents    Multilingual AI
       └─────────────┼─────────────┘
                     ↓
              AI Application
```

Hugging Face models can also be integrated into applications built with frameworks such as **LangChain** and **LlamaIndex**.

---

## ⚙️ Prerequisites

Make sure you have:

* Python 3.9+
* Basic Python knowledge
* Basic understanding of NLP and Generative AI
* Internet access for downloading models

Depending on the example, additional Python packages may be required.

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/TechWithMala/ai-engineering-full-course-for-beginners.git
```

Navigate to this folder:

```bash
cd ai-engineering-full-course-for-beginners/08-huggingface-demo
```

Install the commonly required packages:

```bash
pip install transformers sentence-transformers torch
```

Additional dependencies may be required depending on the specific demo.

---

## ▶️ Run the Examples

Sentence embeddings:

```bash
python SentenceEmbeddings.py
```

Text summarization:

```bash
python SentenceSummarization.py
```

Translation:

```bash
python SentenceTranslation.py
```

Image understanding:

```bash
python ImageUnderstanding.py
```

---

## 🤗 Explore Hugging Face Models

Explore available models on the Hugging Face Hub:

👉 https://huggingface.co/models

You can search for models based on specific tasks, including:

* Embeddings
* Summarization
* Translation
* Text generation
* Image understanding
* Classification
* Speech

Always review the individual model documentation for its requirements, intended use, and license.

---

## 🎯 Recommended Learning Order

If you're new to Hugging Face, follow the examples in this order:

1. `SentenceEmbeddings.py`
2. `SentenceSummarization.py`
3. `SentenceSummarization-2.py`
4. `SentenceTranslation.py`
5. `ImageUnderstanding.py`

This progression moves from **text embeddings → NLP → translation → multimodal AI**.

---

## 📌 Key Takeaways

After completing these examples, you should understand:

* What Hugging Face is
* What pre-trained models are
* How to use Transformer models in Python
* How text can be converted into embeddings
* How AI models can summarize text
* How AI models can translate languages
* How vision-language models can process images
* How Hugging Face models can be used in AI Engineering applications

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
* 🚀 Build your own AI application

Happy Learning! 🤗🚀

