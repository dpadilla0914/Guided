# Guided Project Overview

## Problem Statement

Students use platforms like Canvas to access assignments, grades, and course materials, but when they get stuck on a topic, there is not much built-in support to help them understand the material. Many students end up searching online or using AI tools that give them answers instead of helping them learn how to solve the problem themselves.

---

## Target User

Our target user is a student taking a technical course, such as programming or AI engineering, who wants extra help while studying and needs guidance that helps them understand concepts instead of just getting the answer.

---

## System Explanation

Guided is a learning platform that includes an AI-powered chatbot designed to support students while they learn. When a student asks a question, the system searches through course materials stored in a vector database and returns the most relevant concepts from the curriculum. We also added guardrails to encourage learning and reduce answer-sharing.

The system is built using:

* React for the frontend
* FastAPI for the backend
* ChromaDB for vector storage and retrieval
* Retrieval-Augmented Generation (RAG) concepts for curriculum search

Currently, the system retrieves relevant curriculum content and presents it to students as guidance based on their questions.

---

## Value Statement

Guided helps students learn more effectively by giving them access to course-specific guidance whenever they need it. Instead of replacing the learning process, the platform is designed to support it by helping students find relevant information and better understand the material on their own.
