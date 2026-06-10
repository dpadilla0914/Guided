import { useState } from "react";

export default function ModuleGroup({
  group,
  setSelectedModule,
}) {
  const [open, setOpen] = useState(false);

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
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          fontWeight: "bold",
        }}
      >
        <span>{group.title}</span>

        <span>
          {open ? "▼" : "▶"}
        </span>
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