document
  .getElementById("submit-btn-zdzk")
  .addEventListener("click", function (event) {
    event.preventDefault();
    const input = document.getElementById("zdzk-id").value;
    const data = { idDokumentuZO: input };
    eel.add_zdzk(data)(function (response) {
      document.getElementById("zdzk-response").innerHTML = response;
    });
  });

eel.expose(update_output);
function update_output(data) {
  document.getElementById("zdzk-response").innerHTML = data;
}
