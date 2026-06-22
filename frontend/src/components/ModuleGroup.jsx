import { useState } from "react";

export default function ModuleGroup({ group, setSelectedModule }) {
  const [open, setOpen] = useState(false);
  const progress = group.progress ?? 0;

  return (
    <div className="module-group">
      <div className="group-header" onClick={() => setOpen(!open)}>
        <span className="group-title">{group.title}</span>
        <span className={`group-caret ${open ? "open" : ""}`}>▶</span>
      </div>

      <div className="progress-track">
        <div className="progress-fill" style={{ width: `${progress}%` }} />
      </div>
      <div className="progress-meta">
        <span>{progress}% complete</span>
        {group.completed && <span className="progress-done">✓ Done</span>}
      </div>

      {open && (
        <div className="submodules">
          {group.modules?.map((module) => (
            <div
              key={module.id}
              className="submodule"
              onClick={() => setSelectedModule(module)}
            >
              <span className={`submodule-dot ${module.completed ? "done" : ""}`} />
              <span className="submodule-title">{module.title}</span>
              {module.type && <span className="type-chip">{module.type}</span>}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
