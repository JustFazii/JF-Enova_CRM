document.addEventListener("DOMContentLoaded", function () {
  const addRowButton = document.getElementById("add-row-btn");
  const goodsContainer = document.querySelector(".goods-add-line");
  const submitButton = document.getElementById("submit-doc-btn");
  const contractorInput = document.getElementById("contractor");
  const fetchContractorBtn = document.getElementById("fetch-contractor-btn");
  let activeRowId = sessionStorage.getItem("activeRowId") || null;
  let rowCount = 1;

  const initialRow = document.querySelector(".goods-line");
  if (initialRow) {
    initialRow.dataset.rowId = `row-1`;
    initialRow
      .querySelector(".fetch-goods-btn")
      .addEventListener("click", function () {
        activeRowId = initialRow.dataset.rowId;
        saveRowState();
        sessionStorage.setItem("activeRowId", activeRowId);
        window.location.href = "G_GoodsDocHan.html";
      });
  }

  const selectedContractor = sessionStorage.getItem("selectedContractor");
  if (selectedContractor) {
    contractorInput.value = selectedContractor;
  }

  function createGoodsRow(goods = {}, id = null) {
    rowCount++;
    const rowId = id || `row-${rowCount}`;
    const newRow = document.createElement("div");
    newRow.classList.add("goods-line");
    newRow.dataset.rowId = rowId;
    newRow.innerHTML = `
      <div class="add-doc-goods">
        <input class="add-input-box goods-code" type="text" value="${
          goods.Kod || ""
        }" placeholder="Goods Code"/>
        <input class="add-input-box goods-quantity" type="text" value="${
          goods.Ilosc || ""
        }" placeholder="Quantity"/>
        <input class="add-input-box goods-price" type="text" value="${
          goods.Cena || ""
        }" placeholder="Price"/>
        <button class='fetch-goods-btn' data-row-id="${rowId}"><i class='icon ph-bold ph-magnifying-glass'></i></button>
        <button class='remove-goods-btn'><i class='icon ph-bold ph-trash'></i></button>
      </div>
    `;
    goodsContainer.insertAdjacentElement("beforebegin", newRow);

    const removeButton = newRow.querySelector(".remove-goods-btn");
    removeButton.addEventListener("click", function () {
      newRow.remove();
      saveRowState();
    });

    const fetchGoodsButton = newRow.querySelector(".fetch-goods-btn");
    fetchGoodsButton.addEventListener("click", function () {
      activeRowId = rowId;
      saveRowState();
      sessionStorage.setItem("activeRowId", activeRowId);
      window.location.href = "G_GoodsDocHan.html";
    });
  }

  function saveRowState() {
    const goodsLines = document.querySelectorAll(".goods-line");
    const rowsState = Array.from(goodsLines).map((row) => ({
      rowId: row.dataset.rowId,
      Kod: row.querySelector(".goods-code").value,
      Ilosc: row.querySelector(".goods-quantity").value,
      Cena: row.querySelector(".goods-price").value,
    }));
    sessionStorage.setItem("rowsState", JSON.stringify(rowsState));
  }

  function loadRowState() {
    const rowsState = JSON.parse(sessionStorage.getItem("rowsState"));
    if (rowsState) {
      rowsState.forEach((row) => {
        if (row.rowId === "row-1") {
          const initialRow = document.querySelector(".goods-line");
          if (initialRow) {
            initialRow.querySelector(".goods-code").value = row.Kod;
            initialRow.querySelector(".goods-quantity").value = row.Ilosc;
            initialRow.querySelector(".goods-price").value = row.Cena;
          }
        } else {
          createGoodsRow(row, row.rowId);
        }
      });
    }
  }

  function loadSelectedGoods() {
    const selectedGoods = JSON.parse(sessionStorage.getItem("selectedGoods"));
    if (selectedGoods && selectedGoods.length > 0) {
      selectedGoods.forEach((goods) => {
        if (activeRowId) {
          const goodsRow = document.querySelector(
            `[data-row-id="${activeRowId}"]`
          );
          if (goodsRow) {
            goodsRow.querySelector(".goods-code").value = goods.Kod;
            goodsRow.querySelector(".goods-quantity").value = goods.Ilosc;
            goodsRow.querySelector(".goods-price").value = goods.Cena;
          } else {
            console.error("Active row not found: ", activeRowId);
          }
          activeRowId = null;
          sessionStorage.removeItem("activeRowId");
        } else {
          createGoodsRow(goods);
        }
      });
      sessionStorage.removeItem("selectedGoods");
    } else {
      console.log("No selected goods found");
    }
  }

  function resetForm() {
    contractorInput.value = "";
    const goodsLines = document.querySelectorAll(".goods-line");
    goodsLines.forEach((line, index) => {
      if (index === 0) {
        line.querySelector(".goods-code").value = "";
        line.querySelector(".goods-quantity").value = "";
        line.querySelector(".goods-price").value = "";
      } else {
        line.remove();
      }
    });
    rowCount = 1;
  }

  fetchContractorBtn.addEventListener("click", function () {
    window.location.href = "C_ContractorsDocHan.html";
  });

  addRowButton.addEventListener("click", function () {
    createGoodsRow();
  });

  loadRowState();
  loadSelectedGoods();

  submitButton.addEventListener("click", function () {
    const definicja = document.getElementById("Definicja").value;
    const kontrahent = contractorInput.value;
    const goodsLines = document.querySelectorAll(".goods-line .add-doc-goods");

    const pozycje = Array.from(goodsLines).map((line) => {
      return {
        KodTowaru: line.querySelector(".goods-code").value,
        Ilosc: parseFloat(line.querySelector(".goods-quantity").value),
        Cena: parseFloat(line.querySelector(".goods-price").value),
      };
    });

    const documentData = {
      Definicja: definicja,
      Kontrahent: kontrahent,
      Pozycje: pozycje,
    };

    eel.AddHandelDocument(documentData)(function (response) {
      if (response === "Successfully added document!") {
        sessionStorage.clear();
        resetForm();
      }
      Swal.fire({
        icon: response === "Successfully added document!" ? "success" : "error",
        title: "Response",
        text: response,
      });
    });
  });
});
