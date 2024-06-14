const emitter = mitt();

function selectContractor(contractor) {
  sessionStorage.setItem('selectedContractor', contractor);
  emitter.emit('contractorSelected', contractor);
}

function selectGoods(goods) {
  let selectedGoods = JSON.parse(sessionStorage.getItem('selectedGoods')) || [];
  selectedGoods.push(goods);
  sessionStorage.setItem('selectedGoods', JSON.stringify(selectedGoods));
  emitter.emit('goodsSelected', goods);
}

// Upewnij się, że funkcje są dostępne globalnie
window.selectContractor = selectContractor;
window.selectGoods = selectGoods;
window.emitter = emitter;
