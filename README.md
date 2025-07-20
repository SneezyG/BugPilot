# 🐞 BugPilot, AI Assistant for Bug Ticket Triage

A FastAPI backend that uses AI to classify bug reports and enables semantic search over historical tickets using embeddings and a Vector DB.

## 🚀 Features

- 🧠 Auto-classifies bug tickets (tags, category, summary) using AI
- 🔍 Semantic search using AI powered embeddings + Weaviate(A vector DB)
- ⚡ Stateless, API-first design — easy to integrate into any workflow
- 🧩 AI as a service — Built on AI servives & Exposed as AI services.

## 🏗️ Architecture

Client → FastAPI →  
- `/classify`: Classifies + embeds + stores in Weaviate  
- `/search`: Embeds query → finds similar bugs via vector search

## 🧰 Tech Stack

- **Backend**: FastAPI (Python)
- **LLM**: OpenAI GPT-4
- **Embeddings**: `text-embedding-3-small`
- **Vector DB**: Weaviate (Dockerized)
- **API Style**: REST / JSON

## 📡 API Endpoints

- `POST /classify`: Classifies bug (tags, category, summary) + stores in vector DB
- `POST /search`: Returns semantically similar bugs from history

## 📌 Use Cases

- Auto-tagging and triaging tickets
- Duplicate bug detection
- Semantic search for support/dev teams

## 🧠 Philosophy

- AI as a service  
- AI as a tool, not a black box  
- Modular and swappable components

---
