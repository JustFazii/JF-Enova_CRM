document
  .getElementById("submit-btn-inv-zofv")
  .addEventListener("click", function (event) {
    event.preventDefault();
    const input = document.getElementById("inv-zofv-id").value;
    const data = { idDokumentuZO: input };
    eel.add_zofv_inv(data)(function (response) {
      document.getElementById("inv-zofv-response").innerHTML = response;
    });
  });

eel.expose(update_output);
function update_output(data) {
  document.getElementById("inv-zofv-response").innerHTML = data;
}
