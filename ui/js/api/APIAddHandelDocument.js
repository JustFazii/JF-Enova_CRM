document.addEventListener('DOMContentLoaded', function() {
    const contractorCode = localStorage.getItem('selectedContractorCode');
    console.log('Contractor code from localStorage:', contractorCode); // Debugging log
    if (contractorCode) {
        document.getElementById('contractor').value = contractorCode;
        localStorage.removeItem('selectedContractorCode');
    }

    const selectedGoods = localStorage.getItem('selectedGoods');
    console.log('Selected goods from localStorage:', selectedGoods); // Debugging log
    if (selectedGoods) {
        const { index, KodTowaru, Cena, IloscDostepna } = JSON.parse(selectedGoods);
        const goodsLines = document.querySelectorAll('.goods-line .add-doc-goods');
        if (goodsLines[index]) {
            goodsLines[index].querySelector('.goods-code').value = KodTowaru;
            goodsLines[index].querySelector('.goods-price').value = Cena;
            goodsLines[index].querySelector('.goods-quantity').value = IloscDostepna;
        }
        localStorage.removeItem('selectedGoods');
    }
});
