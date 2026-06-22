import { useState } from "react";
import { students } from "../data/studentData";

export default function AdminSidebar({
  setAdminView,
  setSelectedAdminContent,
}) {
  const [openStudents, setOpenStudents] = useState({});

  const toggleStudent = (studentId) => {
    setOpenStudents((prev) => ({
      ...prev,
      [studentId]: !prev[studentId],
    }));
  };

  return (
    <div className="panel panel-left">
      <div className="brand">
        <div className="brand-mark">G</div>
        <div>
          <div className="brand-name">Guided</div>
          <div className="brand-sub">Instructor Console</div>
        </div>
      </div>

      <div className="eyebrow">Students</div>

      <div className="stagger">
        {students.map((student) => (
          <div key={student.id} className="student-card">
            <div className="student-head" onClick={() => toggleStudent(student.id)}>
              <span className="student-head-left">
                <span className="avatar">{student.name?.[0] ?? "S"}</span>
                {student.name}
              </span>
              <span className={`group-caret ${openStudents[student.id] ? "open" : ""}`}>▶</span>
            </div>

            {openStudents[student.id] && (
              <div className="submodules">
                {student.weeks.map((week) => (
                  <div
                    key={week.title}
                    className="submodule"
                    onClick={() =>
                      setSelectedAdminContent({
                        type: "assignment",
                        student: student.name,
                        ...week,
                      })
                    }
                  >
                    <span className="submodule-dot" />
                    <span className="submodule-title">{week.title}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>

      <div style={{ marginTop: "18px" }}>
        <button className="btn btn-full" onClick={() => setAdminView(false)}>
          Return to Student View
        </button>
      </div>
    </div>
  );
}
