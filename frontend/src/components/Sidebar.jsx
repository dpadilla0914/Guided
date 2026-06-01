import ModuleGroup from "./ModuleGroup";

export default function Sidebar({courseModules=[],setSelectedModule=()=>{},setAdminView=()=>{}}) {
  return (
    <div className="sidebar">
      <div className="sidebar-header"><h2>Course Modules</h2></div>

      {courseModules.map((group) => (
        <ModuleGroup key={group.id} group={group} setSelectedModule={setSelectedModule} />
      ))}

      <div style={{marginTop:"20px"}}>
        <button onClick={() => setAdminView(true)} style={{width:"100%",padding:"12px"}}>
          Admin View
        </button>
      </div>
    </div>
  );
}