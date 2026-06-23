export default function AdminContent({ content }) {
  if (!content)
    return (
      <div className="panel panel-center">
        <div className="empty-state">Select a student item.</div>
      </div>
    );

  return (
    <div className="panel panel-center">
      <div className="content-wrap">
        <span className="module-type">{content.type || "submission"}</span>
        <h1 className="content-title">{content.assignment || content.title}</h1>
        <p className="content-body" style={{ marginBottom: "8px", color: "var(--text-faint)" }}>
          {content.student}
        </p>
        <div className="content-card">
          <p className="content-body" style={{ margin: 0, fontSize: "15px" }}>
            {content.submission || content.text}
          </p>
        </div>
      </div>
    </div>
  );
}
