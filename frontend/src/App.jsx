import { useState } from "react";
import Sidebar from "./components/Sidebar";
import MainContent from "./components/MainContent";
import ChatSidebar from "./components/ChatSidebar";
import AdminSidebar from "./components/AdminSidebar";
import AdminContent from "./components/AdminContent";
import AdminChatSidebar from "./components/AdminChatSidebar";
import { courseModules } from "./data/courseData";

export default function App() {
  const [selectedModule, setSelectedModule] = useState(courseModules[0].modules[0]);
  const [adminView, setAdminView] = useState(false);
  const [selectedAdminContent, setSelectedAdminContent] = useState(null);

  return (
    <div style={{display:"grid",gridTemplateColumns:"320px 1fr 350px",height:"100vh"}}>
      {adminView ? (
        <AdminSidebar setAdminView={setAdminView} setSelectedAdminContent={setSelectedAdminContent} />
      ) : (
        <Sidebar courseModules={courseModules} setSelectedModule={setSelectedModule} setAdminView={setAdminView}/>
      )}

      {adminView ? (
        <AdminContent content={selectedAdminContent} />
      ) : (
        <MainContent module={selectedModule} />
      )}

      {adminView ? (
        <AdminChatSidebar setSelectedAdminContent={setSelectedAdminContent} />
      ) : (
        <ChatSidebar />
      )}
    </div>
  );
}