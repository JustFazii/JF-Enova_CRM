document.addEventListener('DOMContentLoaded', function() {
    eel.GetContractors()(function(html_table) {
        document.getElementById('APIGetContractors').innerHTML = html_table;
        const buttons = document.querySelectorAll('.ShowPosButton');
        buttons.forEach(function(button) {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                const input = button.value;
                eel.GetContractorByID(input)(function(response) {
                    localStorage.setItem('contractorData', JSON.stringify(response));
                    window.location.href = 'C_UpdateContractor.html';
                });
            });
        });
    });
});