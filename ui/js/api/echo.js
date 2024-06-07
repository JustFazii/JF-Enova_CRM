document.getElementById('submit-btn').addEventListener('click', function(event) {
  event.preventDefault();
  const input = document.getElementById('input-box').value;
  eel.send_echo(input)(function(response) {
      document.getElementById('get-echo').innerHTML = response;
  });
});

eel.expose(update_output);
function update_output(data) {
  document.getElementById('get-echo').innerHTML = data;
}