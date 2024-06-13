document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("G_GoodsDocHan.html")) {
      eel.GetGoodsDocHan()(function (data) {
          GetGoodsDocHan(data);
      });

      function GetGoodsDocHan(data) {
          document.getElementById("APIGetGoodsDocHan").innerHTML = data;
          const search = document.querySelector(".input-group input"),
              table_rows = document.querySelectorAll("tbody tr"),
              table_headings = document.querySelectorAll("thead th");

          search.addEventListener("input", searchTable);

          function searchTable() {
              table_rows.forEach((row, i) => {
                  let table_data = row.textContent,
                      search_data = search.value.toLowerCase();

                  row.classList.toggle(
                      "hide",
                      table_data.toLowerCase().indexOf(search_data) < 0
                  );
                  row.style.setProperty("--delay", i / 25 + "s");
              });
          }

          table_headings.forEach((head, i) => {
              let sort_asc = true;
              head.onclick = () => {
                  table_headings.forEach((head) => head.classList.remove("active"));
                  head.classList.add("active");

                  document
                      .querySelectorAll("td")
                      .forEach((td) => td.classList.remove("active"));

                  table_rows.forEach((row) => {
                      row.querySelectorAll("td")[i].classList.add("active");
                  });

                  head.classList.toggle("asc", sort_asc);
                  sort_asc = head.classList.contains("asc") ? false : true;

                  sort_table(i, sort_asc);
              };
          });

          function sort_table(column, sort_asc) {
              [...table_rows]
                  .sort((a, b) => {
                      let first_row = a
                          .querySelectorAll("td")
                          [column].textContent.trim()
                          .toLowerCase(),
                          second_row = b
                          .querySelectorAll("td")
                          [column].textContent.trim()
                          .toLowerCase();

                      let first_num = parseFloat(first_row),
                          second_num = parseFloat(second_row);

                      if (!isNaN(first_num) && !isNaN(second_num)) {
                          return sort_asc ? first_num - second_num : second_num - first_num;
                      }

                      return sort_asc
                          ? first_row > second_row
                              ? 1
                              : -1
                          : first_row > second_row
                              ? -1
                              : 1;
                  })
                  .forEach((sorted_row) =>
                      document.querySelector("tbody").appendChild(sorted_row)
                  );
          }

          document.querySelectorAll('.AddGoodsToHandel').forEach(button => {
              button.addEventListener('click', function() {
                  const goodsId = this.value;
                  console.log('Fetching goods by ID:', goodsId); // Debugging log
                  eel.GetGoodsByID(goodsId)(function(response) {
                      if (response) {
                          console.log('Retrieved goods data:', response); // Debugging log
                          const good = response[0];
                          const currentGoodsLineIndex = localStorage.getItem('currentGoodsLineIndex');
                          console.log('Current goods line index:', currentGoodsLineIndex); // Debugging log
                          localStorage.setItem('selectedGoods', JSON.stringify({
                              index: currentGoodsLineIndex,
                              KodTowaru: good.Kod,
                              Cena: good.Cena,
                              Ilosc: good.IloscDostepna
                          }));
                          localStorage.removeItem('currentGoodsLineIndex');
                          window.location.href = 'D_AddHandelDocument.html';
                      }
                  });
              });
          });
      }
  }
});
