export default function MainContent({ module }) {
  if (!module) {
    return (
      <div className="panel panel-center">
        <div className="empty-state">Select a module to begin.</div>
      </div>
    );
  }

  return (
    <div className="panel panel-center">
      <div className="content-wrap">
        {module.type && <span className="module-type">{module.type}</span>}

        <h1 className="content-title">{module.title}</h1>

        <p className="content-body">{module.content || "No content yet."}</p>

        <div className="content-card">
          <p className="content-body" style={{ fontSize: "15px", margin: 0 }}>
            Stuck? Ask the assistant on the right — it guides you toward the
            answer instead of handing it over.
          </p>
        </div>
      </div>
    </div>
  );
}
