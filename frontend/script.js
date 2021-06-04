let todos = document.getElementById('todos')
let title_input = document.getElementById('id_title')

function addTask(){
    let title = title_input.value
    let data = {
        title : title
    }
    fetch('http://127.0.0.1:8000/api/add-task/',
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    console.log(`A/Az ${title} hozzáadva!`)
    console.log(JSON.stringify(data))
}

refreshData()
function refreshData(){
    fetch('http://127.0.0.1:8000/api/task-list/')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        for(let t in data){

            if(data[t].done){
                task = `<div class="task done">${data[t].title}</div>`
            }else{
                task = `<div class="task">${data[t].title}</div>`
            }
            todos.innerHTML += task
        }
    });
}