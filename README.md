# 🚀 myFirstFastAPI

**myFirstFastAPI** is a simple yet complete example of a modern backend microservice built with **FastAPI**, containerized with **Docker**, and integrated with **GitHub Actions** for continuous integration and deployment.  

It serves as a learning and demonstration project for mastering **DevSecOps fundamentals**, **API design**, and **cloud-ready deployment pipelines**.

---

## 🧩 Features
- 🧱 **FastAPI** backend with structured project layout  
- 🐘 **PostgreSQL** database integration via Docker Compose  
- 🧰 **CI/CD pipeline** using GitHub Actions  
- 🔐 Secure configuration via environment variables  
- 🧪 Example endpoint (`/ask`) to log user input  
- 🐳 Fully containerized for portability and deployment

---

## 🏗️ Architecture Overview
Client → FastAPI (app/main.py)
→ PostgreSQL (db service)
→ Docker Compose (orchestrator)
→ GitHub Actions (CI/CD)


---

## ⚙️ Run Locally

### 1. Clone repo
```bash
git clone https://github.com/<your-username>/myFirstFastAPI.git
cd myFirstFastAPI

### 2. Copy and configure environment variables
cp .env.example .env

### 3. Build and run with Docker Compose
docker-compose up --build

### 4. Visit your local API

Base URL: http://localhost:8000

Health check: / → returns {"message": "Hello from myFirstFastAPI"}

POST endpoint: /ask → accepts JSON { "question": "your query" }


🧠 Purpose

This project is the foundation for Tanggol AI and future DevSecOps experiments.
It provides a minimal working example to practice:

API lifecycle (build → test → deploy)

Secrets management and environment isolation

Infrastructure as Code (Docker Compose, later Terraform)

Continuous Integration / Continuous Deployment (GitHub Actions)

Secure database connectivity

🧭 Next Steps

Add Supabase or PostgreSQL migrations

Implement token-based authentication

Extend CI/CD to push Docker image to AWS or Render

Integrate LLM endpoint (OpenAI / Bedrock) for smart responses

Author: Eric Relleve

AI Architect Partner: Lex (AI-powered project mentor)
License: MIT License


---

“Every great DevSecOps journey starts with one working API.”
