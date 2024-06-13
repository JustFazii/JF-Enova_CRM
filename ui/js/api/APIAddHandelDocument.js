const contractorCode = localStorage.getItem('selectedContractorCode');
    if (contractorCode) {
        document.getElementById('contractor').value = contractorCode;
    }

const selectedGoods = localStorage.getItem('selectedGoods');
    if (selectedGoods) {
        const { index, KodTowaru, Cena, IloscDostepna } = JSON.parse(selectedGoods);
        const goodsLines = document.querySelectorAll('.goods-line .add-doc-goods');
        if (goodsLines[index]) {
            goodsLines[index].querySelector('.goods-code').value = KodTowaru;
            goodsLines[index].querySelector('.goods-price').value = Cena;
            goodsLines[index].querySelector('.goods-quantity').value = IloscDostepna;
        }
    }