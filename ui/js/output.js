document.addEventListener("DOMContentLoaded", function() {
  eel.update_status()(function(data) {
      document.getElementById("status").innerText = data;
  }).catch(function(error) {
      console.error(`Error calling update_status: ${error}`);
  });
}
);

eel.expose(update_output2);
function update_output2(data) {
  document.getElementById("output2").innerHTML = data;
}

document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("contractors.html")) {
    eel.refresh_contractors()(function () {});
  }
});

document.addEventListener("contextmenu", (event) => event.preventDefault());

if (localStorage.getItem("theme") === "dark") {
  document.documentElement.classList.add("dark-theme");
}
