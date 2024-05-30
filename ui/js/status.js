document.addEventListener("DOMContentLoaded", function() {
    if (typeof window.eel === 'undefined') {
      console.error('eel is not defined');
      return;
    }
    eel.update_status()(function(data) {
      document.getElementById("status").innerText = data;
    });
  });