import { useState } from "react";

export default function ChatSidebar() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: "Course AI",
      text: "Hello! Ask me anything about the course.",
    },
  ]);

  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;

    const newMessage = {
      id: Date.now(),
      sender: "Student",
      text: input,
    };

    setMessages((prev) => [...prev, newMessage]);

    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 1,
          sender: "Course AI",
          text: "I can help with assignments, quizzes, and modules.",
        },
      ]);
    }, 500);

    setInput("");
  };

  return (
    <div
      style={{
        borderLeft: "1px solid #ccc",
        display: "flex",
        flexDirection: "column",
        height: "100vh",
        background: "white",
      }}
    >
      <div
        style={{
          padding: "20px",
          borderBottom: "1px solid #ddd",
          fontWeight: "bold",
        }}
      >
        AI Discussion Board
      </div>

      <div
        style={{
          flex: 1,
          overflowY: "auto",
          padding: "20px",
        }}
      >
        {messages.map((msg) => (
          <div
            key={msg.id}
            style={{
              background:
                msg.sender === "Course AI"
                  ? "#e8f1ff"
                  : "#f1f1f1",
              padding: "12px",
              borderRadius: "10px",
              marginBottom: "10px",
            }}
          >
            <strong>{msg.sender}</strong>

            <p>{msg.text}</p>
          </div>
        ))}
      </div>

      <div
        style={{
          display: "flex",
          padding: "15px",
          gap: "10px",
          borderTop: "1px solid #ddd",
        }}
      >
        <input
          type="text"
          value={input}
          placeholder="Message AI..."
          onChange={(e) =>
            setInput(e.target.value)
          }
          onKeyDown={(e) =>
            e.key === "Enter" && sendMessage()
          }
          style={{
            flex: 1,
            padding: "10px",
          }}
        />

        <button onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}