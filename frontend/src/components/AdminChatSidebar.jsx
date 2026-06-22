import { chats } from "../data/conversations";

export default function AdminChatSidebar({ setSelectedAdminContent }) {
  return (
    <div className="panel panel-right">
      <div className="admin-board" style={{ padding: "20px" }}>
        <h3>Student Message Boards</h3>
        <div className="stagger">
          {chats.map((chat) => (
            <div
              key={chat.name}
              className="admin-chat-link"
              onClick={() =>
                setSelectedAdminContent({
                  student: chat.name,
                  title: "Conversation",
                  text: chat.text,
                })
              }
            >
              {chat.name}
            </div>
          ))}
        </div>
      </div>

      <div className="instructor-feed">
        <h3 style={{ fontFamily: "'Bricolage Grotesque', sans-serif", marginBottom: "4px" }}>
          Instructor Team Chat
        </h3>
        <p><b>Professor Adams:</b> Several students are struggling with Week 2.</p>
        <p><b>TA Emily:</b> I will hold extra office hours Thursday.</p>
        <p><b>Professor Adams:</b> Great, let's post an announcement.</p>
      </div>
    </div>
  );
}
