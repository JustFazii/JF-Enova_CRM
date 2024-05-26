/**
 * 
 * @param {HTMLTableElement} table
 * @param {number} column 
 * @param {boolean} asc 
 */

function sortTableByColumn(table, column, asc = true) {
    const dirModifier = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll("tr"));

    const sortedRows = rows.sort((a,b) => {
        const aColText = a.querySelector(`td:nth-child(${column + 1})`).textContent.trim();
        const bColText = b.querySelector(`td:nth-child(${column + 1})`).textContent.trim();

        console.log(aColText);
        console.log(bColText);

    });
}

sortTableByColumn(document.querySelector("table"), 1);