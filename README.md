AI PR Reviewer

An AI-powered tool that automatically reviews GitHub Pull Requests and provides feedback on bugs, security issues, performance issues, and code quality using LLMs.

📌 Features
🔍 Fetches GitHub Pull Request files
🤖 AI-powered code review (DeepSeek / OpenRouter)
🧠 Detects:
Bugs
Security issues
Performance issues
Code smells
⚡ FastAPI backend
🎨 Modern Next.js + Tailwind frontend
📄 File-wise review output
🏗️ Tech Stack
Backend
FastAPI
Python 3.11+
Requests
OpenAI / OpenRouter API
Frontend
Next.js (App Router)
Tailwind CSS
TypeScript
APIs Used
GitHub REST API
DeepSeek / OpenRouter LLM API






📁 Project Structure
reviewai/
│
├── backend/
│   ├── main.py
│   ├── github_service.py
│   ├── ai_reviewer.py
│   └── .env
│
├── frontend/
│   ├── app/
│   │   └── page.tsx
│   ├── components/
│   └── package.json
│
└── README.md





DEMO LINK:
https://www.loom.com/share/5d81c817d07c447487f86b2573bb57eb
