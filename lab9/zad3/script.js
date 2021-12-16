var currentState = 10;

var intervalID = setInterval(() => {
  if (currentState == 1) {
    document.getElementById("licznik").value = 0;
  }
  if (currentState > 0) {
    updateState(currentState - 1);
  }
}, 1000);

function onStateChanged(state) {
  var elements = document.getElementsByTagName("span");
  for (i = 0; i < elements.length; i++) {
    elements[i].textContent = state;
  }
}

function updateState(newState) {
  currentState = newState;
  onStateChanged(currentState);
}

function textChanged() {
  updateState(document.getElementById("licznik").value);
}

//custom elements

class CustomTicker extends HTMLElement {
  intervalID;
  constructor() {
    super();
    this.intervalID = setInterval(() => {
      this.children[0].textContent = currentState;
    }, 1);
    this.innerHTML = `<span>0</span>`;
  }
}

customElements.define("custom-ticker", CustomTicker);
