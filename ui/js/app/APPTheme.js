document.addEventListener("DOMContentLoaded", function() {
    var theme = document.getElementById("theme");

    theme.onclick = function() {
        document.documentElement.classList.toggle("dark-theme");

        if (document.documentElement.classList.contains("dark-theme")) {
            localStorage.setItem("theme", "dark");
        } else {
            localStorage.setItem("theme", "light");
        }
    }
});