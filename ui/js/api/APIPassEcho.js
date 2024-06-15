document
  .getElementById("APIPassEchoButton")
  .addEventListener("click", function (event) {
    event.preventDefault();
    const input = document.getElementById("input-box").value;
    eel.PassEcho(input)(function (response) {
      document.getElementById("APIPassEcho").innerHTML = response;
    });
  });

eel.expose(PassEcho);
function PassEcho(data) {
  document.getElementById("APIPassEcho").innerHTML = data;
}
