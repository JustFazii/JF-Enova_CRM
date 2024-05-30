eel.expose(update_output2);
function update_output2(data) {
  document.getElementById("output2").innerHTML = data;
}

document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("contractors.html")) {
    eel.refresh_contractors()(function(data) {
      update_output2(data);
    });
  }
});

if (localStorage.getItem("theme") === "dark") {
  document.documentElement.classList.add("dark-theme");
}

document.onkeydown = (e) => {
  if (e.ctrlKey && e.shiftKey && e.key == 'I') {
      e.preventDefault();
  }
};