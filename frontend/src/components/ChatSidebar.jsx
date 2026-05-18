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

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userText = input;

    const newMessage = {
      id: Date.now(),
      sender: "Student",
      text: userText,
    };

    // Add user message immediately
    setMessages((prev) => [...prev, newMessage]);
    setInput("");

    try {
      const res = await fetch(
        "https://studious-potato-jj9qg6w4vxpqf5974-8000.app.github.dev/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: userText,
          }),
        }
      );

      if (!res.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await res.json();

      const aiMessage = {
        id: Date.now() + 1,
        sender: "Course AI",
        text: data.reply || "No response from server.",
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 1,
          sender: "Course AI",
          text: "Error: Could not connect to server.",
        },
      ]);
    }
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
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          style={{
            flex: 1,
            padding: "10px",
          }}
        />

        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}