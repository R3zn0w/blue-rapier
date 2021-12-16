var commands = new Map();
commands.set("set", (comm, webStorage) => setGrade(comm, webStorage));
commands.set("showGrades", (comm, webStorage) => showGrades(comm, webStorage));
commands.set("addStudent", (comm, webStorage) => addStudent(comm, webStorage));
var students = new Map();
var storage = window.sessionStorage;

// <student: [[przedmiot, ocena], [przedmiot2, ocena2]]>

function submitForm() {
  var command = document.forms[0].elements.obszar_tekstowy.value;
  var webStorage = document.forms[0].elements.web_storage.checked;
  var splitted = command.split(" ");
  var action = commands.get(splitted[0]);
  if (action == undefined) {
    alert("Wrong command!");
    return;
  }
  action(splitted, webStorage);
}

//comm student przedmiot (ocena)

function doesStudentExist(student, webStorage) {
  if (webStorage) {
    if (storage.getItem(student) != undefined) return true;
    return false;
  } else if (students.get(student) != undefined) return true;
  return false;
}

function setGrade(comm, webStorage) {
  if (!doesStudentExist(comm[1], webStorage)) {
    alert("Student does not exist!");
    return;
  }
  if (webStorage) {
    var studentObj = JSON.parse(storage.getItem(comm[1]));
  } else {
    var studentObj = students.get(comm[1]);
  }

  for (let i = 0; i < studentObj.length; i++) {
    if (studentObj[i].includes(comm[2])) {
      studentObj[i] = [comm[2], comm[3]];
      break;
    } else if (i == studentObj.length - 1) {
      studentObj.push([comm[2], comm[3]]);
    }
  }

  if (webStorage) {
    storage.setItem(comm[1], JSON.stringify(studentObj));
  }
}

function showGrades(comm, webStorage) {
  if (!doesStudentExist(comm[1], webStorage)) {
    alert("Student does not exist!");
    return;
  }
  if (webStorage) {
    var studentObj = JSON.parse(storage.getItem(comm[1]));
  } else {
    var studentObj = students.get(comm[1]);
  }

  var message = `Student ${comm[1]}'s grades: \n`;

  for (let i = 1; i < studentObj.length; i++) {
    message += `Przedmiot: ${studentObj[i][0]}, ocena: ${studentObj[i][1]}\n`;
  }
  alert(message);
}

function addStudent(comm, webStorage) {
  if (doesStudentExist(comm[1], webStorage)) {
    alert("Student exists!");
    return;
  }
  if (webStorage) {
    storage.setItem(comm[1], JSON.stringify([[]]));
  } else {
    students.set(comm[1], [[]]);
  }
}
