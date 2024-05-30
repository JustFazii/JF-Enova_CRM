document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("goods.html")) {
    eel.show_goods()(function(data) {
        show_goods(data);
    })
  }
});

eel.expose(show_goods);
function show_goods(data) {
  document.getElementById("output3").innerHTML = data;
}
