import ModuleGroup from "./ModuleGroup";

export default function Sidebar({
  courseModules = [],
  setSelectedModule = () => {},
}) {
  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h2>Course Modules</h2>
      </div>

      {courseModules.map((group) => (
        <ModuleGroup
          key={group.id}
          group={group}
          setSelectedModule={setSelectedModule}
        />
      ))}
    </div>
  );
}