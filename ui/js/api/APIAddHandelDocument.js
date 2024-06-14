document.addEventListener('DOMContentLoaded', function() {
  const addRowButton = document.getElementById('add-row-btn');
  const goodsContainer = document.querySelector('.goods-add-line');
  const submitButton = document.getElementById('submit-doc-btn');
  const contractorInput = document.getElementById('contractor');
  const fetchContractorBtn = document.getElementById('fetch-contractor-btn');
  let activeRow = null;

  // Załaduj wybranego kontrahenta z sessionStorage
  const selectedContractor = sessionStorage.getItem('selectedContractor');
  if (selectedContractor) {
    contractorInput.value = selectedContractor;
  }

  // Funkcja do tworzenia nowego wiersza towarów
  function createGoodsRow(goods = {}) {
    const newRow = document.createElement('div');
    newRow.classList.add('goods-line');
    newRow.innerHTML = `
      <div class="add-doc-goods">
        <input class="add-input-box goods-code" type="text" value="${goods.Kod || ''}" placeholder="Goods Code"/>
        <input class="add-input-box goods-quantity" type="text" value="${goods.Ilosc || ''}" placeholder="Quantity"/>
        <input class="add-input-box goods-price" type="text" value="${goods.Cena || ''}" placeholder="Price"/>
        <button class='fetch-goods-btn'><i class='icon ph-bold ph-magnifying-glass'></i></button>
        <button class='remove-goods-btn'><i class='icon ph-bold ph-trash'></i></button>
      </div>
    `;
    goodsContainer.insertAdjacentElement('beforebegin', newRow);

    const removeButton = newRow.querySelector('.remove-goods-btn');
    removeButton.addEventListener('click', function() {
      newRow.remove();
    });

    const fetchGoodsButton = newRow.querySelector('.fetch-goods-btn');
    fetchGoodsButton.addEventListener('click', function() {
      activeRow = newRow;
      window.location.href = 'G_GoodsDocHan.html';
    });
  }

  // Funkcja do załadowania wybranych towarów
  function loadSelectedGoods() {
    const selectedGoods = JSON.parse(sessionStorage.getItem('selectedGoods'));
    if (selectedGoods && selectedGoods.length > 0) {
      selectedGoods.forEach(goods => {
        if (activeRow) {
          const goodsRow = activeRow;
          goodsRow.querySelector('.goods-code').value = goods.Kod;
          goodsRow.querySelector('.goods-quantity').value = goods.Ilosc;
          goodsRow.querySelector('.goods-price').value = goods.Cena;
          activeRow = null;
        } else {
          createGoodsRow(goods);
        }
      });
      sessionStorage.removeItem('selectedGoods');
    }
  }

  // Obsługa przycisku wyszukiwania kontrahenta
  fetchContractorBtn.addEventListener('click', function() {
    window.location.href = 'C_ContractorsDocHan.html';
  });

  // Obsługa przycisku dodawania nowego wiersza
  addRowButton.addEventListener('click', function() {
    createGoodsRow();
  });

  // Obsługa przycisku wyszukiwania towaru
  document.querySelectorAll('.fetch-goods-btn').forEach(button => {
    button.addEventListener('click', function() {
      activeRow = button.closest('.goods-line');
      window.location.href = 'G_GoodsDocHan.html';
    });
  });

  // Załaduj wybrane towary po powrocie na stronę
  loadSelectedGoods();

  // Obsługa przycisku wysyłania dokumentu
  submitButton.addEventListener('click', function() {
    const definicja = document.getElementById('Definicja').value;
    const kontrahent = contractorInput.value;
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
