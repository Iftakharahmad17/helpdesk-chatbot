
# Helpdesk Chatbot — Flask + Transformers (AI)  
**by Iftakhar Ahmad — AI & Python Developer**

A production-style, dark-mode chat UI backed by a lightweight AI model (`distilgpt2`) using Hugging Face Transformers.  
Runs locally or deploys free on **Hugging Face Spaces (Docker)**.

## ✨ Features
- Dark/Light theme toggle (remembers preference)
- Sleek chat bubbles and responsive layout
- Flask backend with `/chat` endpoint
- Small AI model for demo-quality responses
- Ready for Docker / Hugging Face Spaces

## 🚀 Run Locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python app.py
# open http://localhost:7860
```

## ☁️ Deploy to Hugging Face Spaces (Docker)
1. Create a Space at https://huggingface.co/spaces → **Create new Space**
   - **SDK:** Docker
   - **Visibility:** Public
2. Push this folder to GitHub and connect the repo to the Space, or upload files directly.
3. Spaces will build using `Dockerfile` and run on port **7860**.

## 📁 Structure
```
helpdesk_chatbot/
├─ app.py
├─ requirements.txt
├─ Dockerfile
├─ templates/
│  └─ index.html
└─ static/
   ├─ style.css
   └─ script.js
```

## 📝 License
MIT
