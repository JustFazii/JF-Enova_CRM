document.addEventListener('DOMContentLoaded', function() {
  if (window.location.pathname.endsWith("D_GetDocumentsPositionsZD.html")) {
    const documentId = localStorage.getItem('documentId');
    if (documentId) {
      eel.GetDocumentsPositions(documentId)(function(response) {
        document.getElementById("APIGetDocumentsPositionsZD").innerHTML = response;
      });
    }
  }
});

eel.expose(GetDocumentsPositions);
function GetDocumentsPositions(response) {
  document.getElementById("APIGetDocumentsPositionsZD").innerHTML = response;
}
