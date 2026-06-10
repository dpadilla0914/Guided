export const courseModules = [
  {
    id: 1,
    title: "Week 1 - Introduction",
    progress: 80,
    completed: false,
    modules: [
      {
        id: 101,
        type: "lesson",
        title: "Welcome to the Course",
        completed: true,
        content:
          "Learn about the course structure, expectations, and grading.",
      },
      {
        id: 102,
        type: "assignment",
        title: "Assignment 1",
        completed: true,
        content:
          "Complete the introductory assignment and submit before Friday.",
      },
      {
        id: 103,
        type: "quiz",
        title: "Quiz 1",
        completed: false,
        content: "Test your understanding of week 1 concepts.",
      },
    ],
  },
  {
    id: 2,
    title: "Week 2 - React Fundamentals",
    progress: 40,
    completed: false,
    modules: [
      {
        id: 201,
        type: "lesson",
        title: "JSX and Components",
        completed: true,
        content:
          "Understand JSX syntax and component-based architecture.",
      },
      {
        id: 202,
        type: "video",
        title: "React State Tutorial",
        completed: false,
        content:
          "Watch the React state management walkthrough video lesson.",
      },
      {
        id: 203,
        type: "assignment",
        title: "Build a Counter App",
        completed: false,
        content:
          "Create a React counter application using useState.",
      },
    ],
  },
  {
    id: 3,
    title: "Week 3 - Advanced Topics",
    progress: 100,
    completed: true,
    modules: [
      {
        id: 301,
        type: "discussion",
        title: "Hooks Discussion",
        completed: true,
        content:
          "Participate in the class discussion about React Hooks.",
      },
      {
        id: 302,
        type: "quiz",
        title: "Advanced Quiz",
        completed: true,
        content:
          "Complete the advanced React concepts assessment.",
      },
    ],
    

  },


  {
    id: 4,
    title: "Week 4 - Backend APIs",
    progress: 70,
    completed: false,
    modules: [
      {
        id: 401,
        type: "lesson",
        title: "Introduction to REST APIs",
        completed: true,
        content:
          "Learn the principles of RESTful API design and HTTP methods.",
      },
      {
        id: 402,
        type: "video",
        title: "FastAPI Crash Course",
        completed: true,
        content:
          "Watch a guided walkthrough of building APIs using FastAPI.",
      },
      {
        id: 403,
        type: "assignment",
        title: "Build a Student API",
        completed: false,
        content:
          "Create CRUD endpoints for managing student records.",
      },
    ],
  },
  {
    id: 5,
    title: "Week 5 - Databases",
    progress: 55,
    completed: false,
    modules: [
      {
        id: 501,
        type: "lesson",
        title: "SQL Fundamentals",
        completed: true,
        content:
          "Learn relational database concepts and SQL queries.",
      },
      {
        id: 502,
        type: "lab",
        title: "Database Setup",
        completed: false,
        content:
          "Configure PostgreSQL and connect it to your application.",
      },
      {
        id: 503,
        type: "assignment",
        title: "Student Records Database",
        completed: false,
        content:
          "Design and implement a database schema for student records.",
      },
    ],
  },
  {
    id: 6,
    title: "Week 6 - Authentication & Security",
    progress: 25,
    completed: false,
    modules: [
      {
        id: 601,
        type: "lesson",
        title: "Authentication Basics",
        completed: true,
        content:
          "Understand sessions, tokens, and authentication workflows.",
      },
      {
        id: 602,
        type: "video",
        title: "JWT Authentication",
        completed: false,
        content:
          "Learn how JSON Web Tokens are used in modern applications.",
      },
      {
        id: 603,
        type: "assignment",
        title: "Secure Your API",
        completed: false,
        content:
          "Add JWT-based authentication to your FastAPI project.",
      },
    ],
  },
  {
    id: 7,
    title: "Week 7 - System Design",
    progress: 10,
    completed: false,
    modules: [
      {
        id: 701,
        type: "lesson",
        title: "Scalability Fundamentals",
        completed: false,
        content:
          "Learn about scaling applications and distributed systems.",
      },
      {
        id: 702,
        type: "discussion",
        title: "WhatsApp System Design",
        completed: false,
        content:
          "Analyze the architecture of a large-scale messaging platform.",
      },
      {
        id: 703,
        type: "assignment",
        title: "Design a Chat Service",
        completed: false,
        content:
          "Create a high-level system design for a messaging application.",
      },
    ],
  },
  {
    id: 8,
    title: "Week 8 - AI Engineering Capstone",
    progress: 0,
    completed: false,
    modules: [
      {
        id: 801,
        type: "lesson",
        title: "RAG Systems Overview",
        completed: false,
        content:
          "Learn retrieval-augmented generation architecture patterns.",
      },
      {
        id: 802,
        type: "project",
        title: "Build a RAG Pipeline",
        completed: false,
        content:
          "Implement document ingestion, retrieval, and answer generation.",
      },
      {
        id: 803,
        type: "presentation",
        title: "Final Project Demo",
        completed: false,
        content:
          "Present your capstone project and explain design decisions.",
      },
    ],
  }
];