document.addEventListener("DOMContentLoaded", function() {
    if (typeof window.eel === 'undefined') {
      console.error('eel is not defined');
      return;
    }
    eel.Status()(function(data) {
      document.getElementById("status").innerText = data;
    });
  });