import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

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

    // Show student message immediately
    setMessages((prev) => [...prev, newMessage]);

    setInput("");

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          student_id: "student_1",
          message: userText,
        }),
      });

      if (!res.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await res.json();

      console.log("Backend response:", data);

      const aiMessage = {
        id: Date.now() + 1,
        sender: "Course AI",
      text:
        data.sources?.join("\n\n") ||
        data.response ||
        "No response from server.",
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error(error);

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
    <div className="panel panel-right">
      <div className="chat-header">
        <div className="chat-orb" />
        <h3>AI Discussion Board</h3>
      </div>

      <div className="messages">
        {messages.map((msg) => {
          const isAi = msg.sender === "Course AI";
          return (
            <div key={msg.id} className={`msg ${isAi ? "msg-ai" : "msg-user"}`}>
              <span className="msg-sender">
                {msg.sender}
                {isAi && <span className="ai-badge">AI</span>}
              </span>
              <p>{msg.text}</p>
            </div>
          );
        })}
      </div>

      <div className="chat-input-bar">
        <input
          className="chat-input"
          type="text"
          value={input}
          placeholder="Message the assistant…"
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button className="chat-send" onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}