export default function MessageBubble({ message }) {
  return (
    <div
      className={`message-bubble ${
        message.type === "ai" ? "ai-message" : ""
      }`}
    >
      <div className="message-header">
        <strong>{message.sender}</strong>

        {message.type === "ai" && (
          <span className="ai-badge">AI</span>
        )}
      </div>

      <p>{message.text}</p>
    </div>
  );
}