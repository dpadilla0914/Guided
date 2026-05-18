import { useState } from "react";
import Sidebar from "./components/Sidebar";
import MainContent from "./components/MainContent";
import ChatSidebar from "./components/ChatSidebar";
import { courseModules } from "./data/courseData";

export default function App() {
  const [selectedModule, setSelectedModule] = useState(
    courseModules[0].modules[0]
  );

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "320px 1fr 350px",
        height: "100vh",
      }}
    >
      <Sidebar
        courseModules={courseModules}
        setSelectedModule={setSelectedModule}
      />

      <MainContent module={selectedModule} />

      <ChatSidebar />
    </div>
  );
}