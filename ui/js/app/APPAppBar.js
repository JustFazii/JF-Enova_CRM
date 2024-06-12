const ipc = window.electron.ipcRenderer;
const maxResBtn = document.getElementById("maxResBtn");
const minimizeBtn = document.getElementById("minimizeBtn");
const closeBtn = document.getElementById("closeBtn");

function changeMaxResBtn(isMaximizedApp) {
  if (isMaximizedApp) {
    maxResBtn.title = "Restore";
    maxResBtn.classList.remove("maximizeBtn");
    maxResBtn.classList.add("restoreBtn");
  } else {
    maxResBtn.title = "Maximize";
    maxResBtn.classList.remove("restoreBtn");
    maxResBtn.classList.add("maximizeBtn");
  }
}

ipc.on("isMaximized", () => {
  changeMaxResBtn(true);
});
ipc.on("isRestored", () => {
  changeMaxResBtn(false);
});

minimizeBtn.addEventListener("click", () => {
  ipc.send("minimizeApp");
});

maxResBtn.addEventListener("click", () => {
  ipc.send("maximizeApp");
});

closeBtn.addEventListener("click", () => {
  ipc.send("closeApp");
});
