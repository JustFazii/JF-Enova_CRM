document.addEventListener("DOMContentLoaded", function() {
  console.log("DOM fully loaded and parsed");
  if (typeof window.eel === 'undefined') {
    console.error('eel is not defined');
    return;
  }
  console.log("Calling eel.update_status...");
  eel.update_status()(function(data) {
    console.log("Data received from update_status:", data);
    document.getElementById("status").innerText = data;
  });
});

eel.expose(update_output2);
function update_output2(data) {
  console.log("Updating output2 with data:", data);
  document.getElementById("output2").innerHTML = data;
}

document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("contractors.html")) {
    console.log("Refreshing contractors...");
    eel.refresh_contractors()(function() {
      console.log("Contractors refreshed.");
    });
  }
});

if (localStorage.getItem("theme") === "dark") {
  document.documentElement.classList.add("dark-theme");
}
