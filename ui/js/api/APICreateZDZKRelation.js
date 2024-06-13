document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
    document.querySelectorAll('.ShowRelationButton').forEach(button => {
        console.log('Adding event listener to button', button);
        button.addEventListener('click', () => {
            console.log('Clicked');
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
