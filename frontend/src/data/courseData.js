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
];