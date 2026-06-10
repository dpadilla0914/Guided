import { students } from "../data/studentData";
export default function AdminSidebar({setAdminView,setSelectedAdminContent}){
return (
<div className="sidebar">
<h2>Students</h2>
{students.map(student=>(
<div key={student.id}>
<h4>{student.name}</h4>
<div>{student.progress}% Complete</div>
{student.weeks.map(week=>(
<div key={week.title} style={{cursor:"pointer",marginLeft:"15px"}}
onClick={()=>setSelectedAdminContent({type:"assignment",student:student.name,...week})}>
{week.title}
</div>
))}
</div>
))}
<button onClick={()=>setAdminView(false)}>Return to Student View</button>
</div>
)}