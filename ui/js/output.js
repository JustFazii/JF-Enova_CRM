eel.expose(update_output2);
function update_output2(data) {
  document.getElementById("output2").innerHTML = data;
  const search = document.querySelector('.input-group input'),
    table_rows = document.querySelectorAll('tbody tr');

search.addEventListener('input', searchTable);

console.log(search)
console.log(table_rows)

function searchTable() {
    table_rows.forEach( (row,i )=> {
        let table_data = row.textContent,
        search_data = search.value;
        
        console.log(table_data);
        console.log(search_data);

        console.log(table_data.indexOf(search_data) < 0)
        row.classList.toggle('hide', table_data.indexOf(search_data) < 0);
        row.style.setProperty('--delay', i/25 + 's')
    })
}
}

document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("contractors.html")) {
    eel.refresh_contractors()(function(data) {
      update_output2(data);
        const search = document.querySelector('.input-group input'),
      table_rows = document.querySelectorAll('tbody tr');

  search.addEventListener('input', searchTable);

  console.log(search)
  console.log(table_rows)

  function searchTable() {
      table_rows.forEach( (row,i )=> {
          let table_data = row.textContent,
          search_data = search.value;
          
          console.log(table_data);
          console.log(search_data);

          console.log(table_data.indexOf(search_data) < 0)
          row.classList.toggle('hide', table_data.indexOf(search_data) < 0);
          row.style.setProperty('--delay', i/25 + 's')
      })
  }
    });
  }
});

if (localStorage.getItem("theme") === "dark") {
  document.documentElement.classList.add("dark-theme");
}

// document.onkeydown = (e) => {
//   if (e.ctrlKey && e.shiftKey && e.key == 'I') {
//       e.preventDefault();
//   }
// };