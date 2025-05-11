# AI-Powered SQL Query Generator

This project allows users to upload a SQL schema and query it using natural language. It uses a locally hosted large language model (LLM) running via Ollama on an EC2 instance to translate plain English questions into valid SQL queries.

---

## 🧠 Features

- Upload your custom SQL schema
- Ask questions in natural language
- Returns SQL queries tailored to your schema
- Hosted locally using [Ollama](https://ollama.com) and Mistral 7B (quantized)
- Built with React (frontend) + Flask (backend)

---

## 📦 Technologies

- Python (Flask)
- React (Vite)
- Ollama + Mistral 7B (`q4_K_M`)
- AWS EC2 (c6i.2xlarge)
- Postman / Python `requests` for testing

---

## 🚀 How to Use

### 1. Start the Ollama server on your EC2 instance:

```bash
ollama run mistral:7b-instruct-q4_K_M
