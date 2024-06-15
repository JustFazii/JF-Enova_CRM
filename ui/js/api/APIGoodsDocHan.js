document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("G_GoodsDocHan.html")) {
    eel.GetGoodsDocHan()(function (data) {
      GetGoodsDocHan(data);
    });

    function GetGoodsDocHan(data) {
      document.getElementById("APIGetGoodsDocHan").innerHTML = data;

      const addGoodsButtons = document.querySelectorAll(".AddGoodsToHandel");
      addGoodsButtons.forEach((button) => {
        button.addEventListener("click", function () {
          const goodsId = this.value;
          eel.GetGoodsByID(goodsId)(function (data) {
            if (data && data.length > 0) {
              const goods = {
                Kod: data[0].Kod,
                Cena: data[0].Cena,
                Ilosc: data[0].IloscDostepna,
              };
              selectGoods(goods);
              window.location.href = "D_AddHandelDocument.html";
            } else {
              alert("Unable to find goods.");
            }
          });
        });
      });
    }
  }
});
