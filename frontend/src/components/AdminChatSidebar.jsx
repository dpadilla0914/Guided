import { chats } from "../data/conversations";

export default function AdminChatSidebar({setSelectedAdminContent}){
return (
<div style={{borderLeft:"1px solid #ccc",display:"flex",flexDirection:"column"}}>
<div style={{padding:"15px",borderBottom:"1px solid #ccc"}}>
<h3>Student Message Boards</h3>
{chats.map(chat=>(
<div key={chat.name} style={{cursor:"pointer"}}
onClick={()=>setSelectedAdminContent({student:chat.name,title:"Conversation",text:chat.text})}>
{chat.name}
</div>
))}
</div>

<div style={{padding:"15px"}}>
<h3>Instructor Team Chat</h3>
<p><b>Professor Adams:</b> Several students are struggling with Week 2.</p>
<p><b>TA Emily:</b> I will hold extra office hours Thursday.</p>
<p><b>Professor Adams:</b> Great, let's post an announcement.</p>
</div>
</div>
);
}