document
  .getElementById("submit-btn-zofv")
  .addEventListener("click", function (event) {
    event.preventDefault();
    const input = document.getElementById("zofv-id").value;
    const data = { idDokumentuZO: input };
    eel.add_zofv(data)(function (response) {
      document.getElementById("zofv-response").innerHTML = response;
    });
  });

eel.expose(update_output);
function update_output(data) {
  document.getElementById("zofv-response").innerHTML = data;
}
