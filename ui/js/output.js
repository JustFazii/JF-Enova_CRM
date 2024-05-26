eel.expose(update_status);
function update_status(data) {
  document.getElementById("status").innerText = data;
}

eel.expose(update_output2);
function update_output2(data) {
  document.getElementById("output2").innerHTML = data;
}

document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("contractors.html")) {
    eel.refresh_contractors()(function () {});
  }
});

document.addEventListener('contextmenu', event => event.preventDefault());