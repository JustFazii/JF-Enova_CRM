document
  .getElementById("submit-btn-inv-zdzk")
  .addEventListener("click", function (event) {
    event.preventDefault();
    const input = document.getElementById("inv-zdzk-id").value;
    const data = { idDokumentuZO: input };
    eel.add_zdzk_inv(data)(function (response) {
      document.getElementById("inv-zdzk-response").innerHTML = response;
    });
  });

eel.expose(update_output);
function update_output(data) {
  document.getElementById("inv-zdzk-response").innerHTML = data;
}
