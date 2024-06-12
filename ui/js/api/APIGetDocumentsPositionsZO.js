document.addEventListener('DOMContentLoaded', function() {
  if (window.location.pathname.endsWith("D_GetDocumentsPositionsZO.html")) {
    const documentId = localStorage.getItem('documentId'); // Pobieranie właściwej wartości z localStorage
    if (documentId) {
      eel.GetDocumentsPositions(documentId)(function(response) {
        document.getElementById("APIGetDocumentsPositionsZO").innerHTML = response;
      });
    }
  }
});

eel.expose(GetDocumentsPositions);
function GetDocumentsPositions(response) {
  document.getElementById("APIGetDocumentsPositionsZO").innerHTML = response;
}
