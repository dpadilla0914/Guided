export default function MainContent({ module }) {
  if (!module) {
    return (
      <div style={{ padding: "30px" }}>
        No module selected
      </div>
    );
  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>{module.title}</h1>

      <p style={{ marginTop: "20px" }}>
        {module.content || "No content yet"}
      </p>
    </div>
  );
}