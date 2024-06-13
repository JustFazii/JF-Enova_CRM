document.addEventListener('DOMContentLoaded', function() {
    const addRowButton = document.getElementById('add-row-btn');
    const goodsContainer = document.querySelector('.goods-add-line');
    const submitButton = document.getElementById('submit-doc-btn');

    function addFetchGoodsButtonEvent(fetchGoodsButton, row) {
        fetchGoodsButton.addEventListener('click', function() {
            const index = Array.from(goodsContainer.parentElement.children).indexOf(row);
            console.log('Saving index to localStorage:', index); // Debugging log
            localStorage.setItem('currentGoodsLineIndex', index);
            window.location.href = 'G_GoodsDocHan.html';
        });
    }

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

        const fetchGoodsButton = newRow.querySelector('.fetch-goods-btn');
        addFetchGoodsButtonEvent(fetchGoodsButton, newRow);

        const removeButton = newRow.querySelector('.remove-goods-btn');
        removeButton.addEventListener('click', function() {
            newRow.remove();
        });
    });

    // Add event listeners to existing rows
    document.querySelectorAll('.fetch-goods-btn').forEach((button, index) => {
        const row = button.closest('.goods-line');
        addFetchGoodsButtonEvent(button, row);
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

document.addEventListener('DOMContentLoaded', function() {
    // Retrieve and populate goods data from localStorage
    const selectedGoods = localStorage.getItem('selectedGoods');
    console.log('Selected goods from localStorage:', selectedGoods); // Debugging log
    if (selectedGoods) {
        const { index, KodTowaru, Cena, Ilosc } = JSON.parse(selectedGoods);
        console.log('Retrieved selected goods:', { index, KodTowaru, Cena, Ilosc }); // Debugging log
        const goodsLines = document.querySelectorAll('.goods-line .add-doc-goods');
        if (goodsLines[index]) {
            goodsLines[index].querySelector('.goods-code').value = KodTowaru;
            goodsLines[index].querySelector('.goods-price').value = Cena;
            goodsLines[index].querySelector('.goods-quantity').value = Ilosc;
        } else {
            console.log('Goods line at index not found:', index); // Debugging log
        }
        localStorage.removeItem('selectedGoods');
    }

    // Retrieve and populate contractor code from localStorage
    const contractorCode = localStorage.getItem('selectedContractorCode');
    console.log('Contractor code from localStorage:', contractorCode); // Debugging log
    if (contractorCode) {
        document.getElementById('contractor').value = contractorCode;
        localStorage.removeItem('selectedContractorCode');
    }
});
