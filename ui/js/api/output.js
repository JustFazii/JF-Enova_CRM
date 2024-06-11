eel.expose(update_output4);
function update_output4(data) {
  document.getElementById("output4").innerHTML = data;
}





document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("getdocumentsZO.html")) {
    eel.update_output4()(function (data) {
      update_output4(data);
    });
  } else if (window.location.pathname.endsWith("getdocumentsZD.html")) {
    eel.update_output5()(function (data) {
      update_output5(data);
    });
  }
});


if (localStorage.getItem("theme") === "dark") {
  document.documentElement.classList.add("dark-theme");
}

document.onkeydown = (e) => {
  if (e.ctrlKey && e.shiftKey && e.key == "I") {
    e.preventDefault();
  }
};
