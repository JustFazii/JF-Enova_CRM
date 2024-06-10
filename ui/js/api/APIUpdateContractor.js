document.addEventListener('DOMContentLoaded', function() {
    eel.GetContractors()(function(html_table) {
        document.getElementById('APIGetContractors').innerHTML = html_table;
        const buttons = document.querySelectorAll('.ShowPosButton');
        buttons.forEach(function(button) {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                const input = button.value;
                eel.GetContractorByID(input)(function(response) {
                    console.log('Received data:', response);  // Debugging line
                    localStorage.setItem('contractorData', JSON.stringify(response));
                    console.log('Stored data in localStorage:', localStorage.getItem('contractorData'));  // Debugging line
                    window.location.href = 'C_UpdateContractor.html';
                });
            });
        });
    });
});