function login(){
window.location="dashboard.html";
}

function openFaculty(){

window.location.href = "faculty.html"

}
function loadTimetable() {
fetch("/timetable")
.then (reponse => Response.json())
.then(data => {
    console.log(data);
    let table = document.getElementById("tableBody");
    data.forEach(row =>{
        table.innerHTML +=
        <tr>
            <td>${row.class}</td>
            <td>${row.subjects}</td>
            <td>${row.faculty}</td>
            <td>${row.room}</td>
            <td>${row.day}</td>
            <td>${row.time}</td>
        </tr>
        ;
    });
})
.catch(error => console.log(error));
}
<button onclick="generate()">Generate Timetable</button>

//Generate timetable
function generate() {
    fetch("/generate")
    .then(res => res.json())
    .then(data => {
        alert("Generated Successfully!");
        loadTimetable();
        location.reload();
    });
}

window.onload = loadTimetable;
