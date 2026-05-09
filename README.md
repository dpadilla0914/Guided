# Guided

## Team Members
```
Dave Padilla
Raymond Lin
Tashoy Miller testing my branch - Tashoy
```

## Project Description
```
Guided is a private RAG-powered learning assistant designed for cohort-based technical programs.

The system retrieves curriculum content and generates guided, Socratic-style responses without providing direct answers. It also provides administrators with insight into student engagement, struggle patterns, and curriculum gaps through logging and analytics.
```

## Tech Stack

### Backend
```
Python
FastAPI
```

### Retrieval / AI
```
ChromaDB
OpenAI Embeddings
GPT-4 / Claude API
```

### Frontend
```
React / Streamlit
```

### DevOps
```
GitHub Actions
```

## Setup

### Backend Setup

```powershell
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Architecture Diagram

See:
docs/architecture_diagram.png
