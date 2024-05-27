document.getElementById('submit-btn').addEventListener('click', function(event) {
  event.preventDefault();
  const input = document.getElementById('input-box').value;
  console.log("Sending request with value:", input);
  eel.send_echo(input)(function(response) {
      console.log("Received response:", response);
      document.getElementById('get-echo').innerHTML = response;
  }).catch(err => console.error("Error in eel.send_request:", err));
});

eel.expose(update_output);
function update_output(data) {
  document.getElementById('get-echo').innerHTML = data;
}
