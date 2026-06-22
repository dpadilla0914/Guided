import ModuleGroup from "./ModuleGroup";

export default function Sidebar({courseModules=[],setSelectedModule=()=>{},setAdminView=()=>{}}) {
  return (
    <div className="panel panel-left">
      <div className="brand">
        <div className="brand-mark">G</div>
        <div>
          <div className="brand-name">Guided</div>
          <div className="brand-sub">Socratic Learning</div>
        </div>
      </div>

      <div className="eyebrow">Course Modules</div>

      <div className="stagger">
        {courseModules.map((group) => (
          <ModuleGroup key={group.id} group={group} setSelectedModule={setSelectedModule} />
        ))}
      </div>

      <div style={{marginTop:"18px"}}>
        <button className="btn btn-full" onClick={() => setAdminView(true)}>
          Admin View
        </button>
      </div>
    </div>
  );
}
