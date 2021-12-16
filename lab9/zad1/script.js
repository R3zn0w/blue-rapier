var boxed_elements = [];
var column_elements = [];

boxed_elements.push(document.getElementById("box1"));
boxed_elements.push(document.getElementById("box2"));
boxed_elements.push(document.getElementById("box3"));
boxed_elements.push(document.getElementById("box4"));
boxed_elements.push(document.getElementById("box5"));

column_elements.push(document.getElementById("column1"));
column_elements.push(document.getElementById("column2"));

function setElements() {
  for (i = 0; i < boxed_elements.length; i++) {
    boxed_elements[i].classList.add("box");
  }

  for (i = 0; i < column_elements.length; i++) {
    column_elements[i].classList.add("column");
  }

  document.getElementById("body").classList.add("body");
  document.getElementById("container").classList.add("container");
  document.getElementById("box2").classList.add("nav");
  document.getElementById("box3").classList.add("main");
  document.getElementById("box4").classList.add("aside");
  document.getElementById("h1").classList.add("nav_title");
}

function resetElements() {
  for (i = 0; i < boxed_elements.length; i++) {
    boxed_elements[i].classList.remove("box");
  }

  for (i = 0; i < column_elements.length; i++) {
    column_elements[i].classList.remove("column");
  }

  document.getElementById("body").classList.remove("body");
  document.getElementById("container").classList.remove("container");
  document.getElementById("box2").classList.remove("nav");
  document.getElementById("box3").classList.remove("main");
  document.getElementById("box4").classList.remove("aside");
  document.getElementById("h1").classList.remove("nav_title");
}
