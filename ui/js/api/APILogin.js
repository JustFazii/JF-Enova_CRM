document.addEventListener("DOMContentLoaded", function () {
  const signInButton = document.getElementById("sign-in-button");

  signInButton.addEventListener("click", function (event) {
    event.preventDefault();

    const token = document.getElementById("sign-in-input").value;

    eel.Login(token)(function (result) {
      if (result && typeof result === "string" && result.startsWith("Error")) {
        Swal.fire({
          icon: "error",
          title: "Login failed",
          text: result,
        });
      } else {
        localStorage.removeItem("timeLeft");
        localStorage.removeItem("timerEnd");
        window.location.href = "index.html";
      }
    });
  });
});
