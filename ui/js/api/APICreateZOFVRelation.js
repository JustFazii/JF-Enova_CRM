document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.ShowRelationButton').forEach(button => {
        button.addEventListener('click', () => {
            let documentId = button.value;
            showRelation(documentId);
        });
    });
});

function showRelation(documentId) {
    eel.CreateZDZKRelation(documentId)(function(result) {
        alert(result);
    });
}