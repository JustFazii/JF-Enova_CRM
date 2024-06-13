document.addEventListener('DOMContentLoaded', function() {
    const addRowButton = document.getElementById('add-row-btn');
    const goodsContainer = document.querySelector('.goods-add-line');
  
    addRowButton.addEventListener('click', function() {
      const newRow = document.createElement('div');
      newRow.classList.add('goods-line');
  
      newRow.innerHTML = `
        <div class="add-doc-goods">
          <input class="add-input-box goods-code" type="text" placeholder="Goods Code"/>
          <input class="add-input-box goods-quantity" type="text" placeholder="Quantity"/>
          <input class="add-input-box goods-price" type="text" placeholder="Price"/>
          <button class='add-doc-goods-btn'><i class='icon ph-bold ph-list-plus'></i></button>
          <button class='remove-goods-btn'><i class='icon ph-bold ph-trash'></i></button>
        </div>
      `;
  
      goodsContainer.insertAdjacentElement('beforebegin', newRow);
  
      const removeButton = newRow.querySelector('.remove-goods-btn');
      removeButton.addEventListener('click', function() {
        newRow.remove();
      });
    });
  });