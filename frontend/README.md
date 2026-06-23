# Education Platform

A modern React educational platform inspired by Canvas and Blackboard.

Features include:

- Left sidebar learning modules
- Expandable weekly cohorts
- Progress bars and completion tracking
- Assignments, quizzes, videos, and lessons
- Main content learning area
- AI-powered discussion/chat sidebar
- Responsive dashboard layout
- React + Vite architecture

---

# Tech Stack

- React
- Vite
- JavaScript
- CSS
- Lucide React Icons

---

# Project Structure

```txt
frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── Sidebar.jsx
│   │   ├── ModuleGroup.jsx
│   │   ├── MainContent.jsx
│   │   ├── ChatSidebar.jsx
│   │   └── Header.jsx
│   │
│   ├── data/
│   │   └── courseData.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── package.json
├── vite.config.js
└── README.md
```

---

# Requirements

Install:

- Node.js
- npm
- Visual Studio Code

Recommended VS Code Extensions:

- ES7+ React snippets
- Prettier
- ESLint

---

# Installation

Clone project or open folder in VS Code.

Install dependencies:

```bash
npm install
```

---

# Start Development Server

Run:

```bash
npm run dev
```

Vite will start the app.

Open browser:

```txt
http://localhost:5173
```

---

# Start tunnel-deployment,

C:\Users\BOSSE\source\repos\Guided\ngrok-v3-stable-windows-amd64.\ngrok.exe http 5173

Go to website (it may change):
https://nearest-uncross-verify.ngrok-free.dev/

# Build for Production

```bash
npm run build
```

---

# Main Features

## Left Sidebar

- Weekly learning groups
- Expandable dropdown modules
- Progress tracking
- Completion checkmarks

## Main Content Area

- Lesson display
- Assignments
- Quiz information
- Video modules

## Right AI Chat Sidebar

- Discussion board
- AI assistant replies
- Student messaging
- Real-time style chat interface

---

# Common Issues

## Blank White Screen

Usually caused by:

- missing imports
- invalid JSX
- capitalization mismatch in file names
- undefined props

Open browser console:

```txt
F12 → Console
```

to view React errors.

---

## Vite Cache Problems

Delete cache:

```bash
rm -rf node_modules/.vite
```

Restart server:

```bash
npm run dev
```

---

## Dependency Problems

Delete:

```txt
node_modules
package-lock.json
```

Then reinstall:

```bash
npm install
```

---

# Future Improvements

- Real backend integration
- Database support
- Authentication/login
- Real AI API integration
- Notifications
- Video streaming
- Assignment submissions
- Grades dashboard
- Mobile responsive layout

---

# Author

Built with React + Vite.