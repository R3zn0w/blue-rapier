var commands = new Map();
commands.set("set", (comm, webStorage)=> setGrade(comm, webStorage));
commands.set("showGrades", (comm, webStorage)=> showGrades(comm, webStorage));
commands.set("addStudent", (comm, webStorage)=> addStudent(comm, webStorage));
var students = new Map();
var storage = window.localStorage;

// <student: [[przedmiot, ocena], [przedmiot2, ocena2]]>

function submitForm(){
    var command = document.forms[0].elements.obszar_tekstowy.value
    var webStorage = document.forms[0].elements.web_storage.checked
    var splitted = command.split(" ");
    var action = commands.get(splitted[0])
    if ( action == undefined){
        alert("Wrong command!")
        return
    }
    action(splitted, webStorage)
    console.log(command);
    console.log(webStorage);
}

//comm student przedmiot (ocena)

function setGrade(comm, webStorage){
    if(webStorage){
        if(storage.getItem(comm[1]) == undefined){
            alert("no such student!")
            return
        }
        var studentObj = storage.getItem(comm[1])

    }
    else{
        if(students.get(comm[1]) == undefined){
            alert("no such student!")
            return
        }
        var studentObj = students.get(comm[1])

//        students.set(comm[1], [[]])
    } 
    
    for (let i = 0; i < studentObj.length; i++){
        if (studentObj[i].includes(comm[2])){
            studentObj[i] = [comm[2], comm[3]];
            break
        }
        else if (i == studentObj.length-1){
        studentObj.push([comm[2], comm[3]])
        }
    }

    if (webStorage){
        storage.setItem(comm[1], studentObj)
    }

    console.log(students)
    console.log(storage)
    
}


function showGrades(comm, webStorage){}

function addStudent(comm, webStorage){
    if (webStorage){
        if(storage.getItem(comm[1]) != undefined){
            alert("Student exists!")
            return
        }
        storage.setItem(comm[1], [[]])
    }

    else {
        if(students.get(comm[1]) != undefined){
            alert("Student exists!")
            return
        }
        students.set(comm[1], [[]])
    }

}
