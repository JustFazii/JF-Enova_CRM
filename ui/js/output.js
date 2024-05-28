document.addEventListener("DOMContentLoaded", function() {
  if (typeof window.eel === 'undefined') {
    console.error('eel is not defined');
    return;
  }
  eel.update_status()(function(data) {
    document.getElementById("status").innerText = data;
  });
});

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