import { useState } from "react";

export default function ModuleGroup({
  group,
  setSelectedModule,
}) {
  const [open, setOpen] = useState(true);

  if (!group) return null;

  return (
    <div
      style={{
        border: "1px solid #ccc",
        marginBottom: "10px",
        padding: "10px",
      }}
    >
      <div
        onClick={() => setOpen(!open)}
        style={{
          cursor: "pointer",
          fontWeight: "bold",
        }}
      >
        {group.title}
      </div>

      {open &&
        group.modules?.map((module) => (
          <div
            key={module.id}
            onClick={() =>
              setSelectedModule(module)
            }
            style={{
              marginLeft: "20px",
              marginTop: "10px",
              cursor: "pointer",
            }}
          >
            {module.title}
          </div>
        ))}
    </div>
  );
}