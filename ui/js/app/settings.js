document.onkeydown = (e) => {
  if (e.ctrlKey && e.shiftKey && e.key == "I") {
    e.preventDefault();
  }
};
