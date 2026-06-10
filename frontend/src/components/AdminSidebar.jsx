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
    <div className="sidebar">
      <div className="sidebar-header">
        <h2>Students</h2>
      </div>

      {students.map((student) => (
        <div
          key={student.id}
          style={{
            border: "1px solid #ccc",
            marginBottom: "10px",
            padding: "10px",
          }}
        >
          <div
            onClick={() => toggleStudent(student.id)}
            style={{
              fontWeight: "bold",
              cursor: "pointer",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <span>{student.name}</span>

            <span>
              {openStudents[student.id] ? "▼" : "▶"}
            </span>
          </div>

          {openStudents[student.id] &&
            student.weeks.map((week) => (
              <div
                key={week.title}
                onClick={() =>
                  setSelectedAdminContent({
                    type: "assignment",
                    student: student.name,
                    ...week,
                  })
                }
                style={{
                  marginLeft: "20px",
                  marginTop: "10px",
                  cursor: "pointer",
                }}
              >
                {week.title}
              </div>
            ))}
        </div>
      ))}

      <div style={{ marginTop: "20px" }}>
        <button
          onClick={() => setAdminView(false)}
          style={{
            width: "100%",
            padding: "12px",
          }}
        >
          Return to Student View
        </button>
      </div>
    </div>
  );
}