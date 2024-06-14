document.addEventListener('DOMContentLoaded', function() {
    const addRowButton = document.getElementById('add-row-btn');
    const goodsContainer = document.querySelector('.goods-add-line');
    const submitButton = document.getElementById('submit-doc-btn');

    addRowButton.addEventListener('click', function() {
        const newRow = document.createElement('div');
        newRow.classList.add('goods-line');

        newRow.innerHTML = `
            <div class="add-doc-goods">
                <input class="add-input-box goods-code" type="text" placeholder="Goods Code"/>
                <input class="add-input-box goods-quantity" type="text" placeholder="Quantity"/>
                <input class="add-input-box goods-price" type="text" placeholder="Price"/>
                <button class='fetch-goods-btn'><i class='icon ph-bold ph-magnifying-glass'></i></button>
                <button class='remove-goods-btn'><i class='icon ph-bold ph-trash'></i></button>
            </div>
        `;

        goodsContainer.insertAdjacentElement('beforebegin', newRow);

        const removeButton = newRow.querySelector('.remove-goods-btn');
        removeButton.addEventListener('click', function() {
            newRow.remove();
        });
    });

    submitButton.addEventListener('click', function() {
        const definicja = document.getElementById('Definicja').value;
        const kontrahent = document.getElementById('contractor').value;
        const goodsLines = document.querySelectorAll('.goods-line .add-doc-goods');

        const pozycje = Array.from(goodsLines).map(line => {
            return {
                KodTowaru: line.querySelector('.goods-code').value,
                Ilosc: parseFloat(line.querySelector('.goods-quantity').value),
                Cena: parseFloat(line.querySelector('.goods-price').value)
            };
        });

        const documentData = {
            Definicja: definicja,
            Kontrahent: kontrahent,
            Pozycje: pozycje
        };

        eel.AddHandelDocument(documentData)(function(response) {
            alert(response);
        });
    });
});
