document.addEventListener("DOMContentLoaded", function() {
    var theme = document.getElementById("theme");

    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-theme");
    }

    theme.onclick = function() {
        document.body.classList.toggle("dark-theme");
        
        if (document.body.classList.contains("dark-theme")) {
            localStorage.setItem("theme", "dark");
        } else {
            localStorage.setItem("theme", "light");
        }
    }
});