document.addEventListener("DOMContentLoaded", function() {
    if (typeof window.eel === 'undefined') {
      console.error('eel is not defined');
      return;
    }
    eel.GetSettings()(function(data) {
        document.getElementById('sign-in-input').value = data.USER_TOKEN || '';
        document.getElementById('ip').value = data.IP || '';
        document.getElementById('port').value = data.PORT || '';
    });
});
