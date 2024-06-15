document.addEventListener("DOMContentLoaded", function () {
  const saveSettingsButton = document.getElementById("save-settings-button");

  saveSettingsButton.addEventListener("click", function (event) {
    event.preventDefault();

    const ip = document.getElementById("ip").value;
    const port = document.getElementById("port").value;

    eel.SetSettings(
      ip,
      port
    )(function (result) {
      Swal.fire({
        icon: "success",
        title: "Settings Saved",
        text: "Settings have been saved successfully.",
      });
    });
  });
});
