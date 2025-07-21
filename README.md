# 🐞 BugPilot: AI Assistant for Bug Ticket Triage.

A Intelligent system that uses AI to classify bug reports and enables semantic search over historical tickets using embeddings and a Vector DB.

## [See BugPilot Code Repo](https://github.com/SneezyG/BugPilot)

---

## 🚀 Features

- 🧠 Auto-classifies bug tickets (tags, category, summary) using AI
- 🔍 Semantic search using AI powered embeddings + Weaviate(A vector DB)
- ⚡ Stateless, API-first design — easy to integrate into any workflow
- 🧩 AI as a service — Built on AI servives & Exposed as AI services.

---

## 📌 Use Cases

- **Auto-tagging and triaging tickets** – Automatically classifies and prioritizes bug reports using AI-driven tagging and severity assessment.
- **Duplicate bug detection** – Identifies and links similar or repeated issues by comparing bug descriptions semantically.
- **Semantic search for support/dev teams** – Enables natural language search over historical tickets for faster issue resolution and reference.

---

## 🏗️ Architecture

Client → FastAPI →  
- `/classify`: Classifies + embeds + stores in Weaviate  
- `/search`: Embeds query → finds similar bugs via vector search

---

## 🧰 Tech Stack

- **Backend**: FastAPI (Python)
- **LLM**: OpenAI GPT-4
- **Embeddings**: `text-embedding-3-small`
- **Vector DB**: Weaviate (Dockerized)
- **API Style**: REST / JSON

---

## 📡 API Endpoints

- `POST /classify`: Classifies bug (tags, category, summary) + stores in vector DB
- `POST /search`: Returns semantically similar bugs from history

---

## 🧠 Philosophy

- AI as a service  
- AI as a tool, not a black box  
- Modular and swappable components

---
