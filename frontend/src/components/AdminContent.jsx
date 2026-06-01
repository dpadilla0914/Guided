export default function AdminContent({content}){
if(!content) return <div style={{padding:"30px"}}>Select a student item.</div>;
return (
<div style={{padding:"30px"}}>
<h2>{content.student}</h2>
<h3>{content.assignment || content.title}</h3>
<p>{content.submission || content.text}</p>
</div>
);
}