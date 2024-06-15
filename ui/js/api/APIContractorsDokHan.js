document.addEventListener("DOMContentLoaded", function () {
  eel.GetContractorsDokHan()(function (html_table) {
    document.getElementById("APIGetContractorsDokHan").innerHTML = html_table;

    const addContractorButtons = document.querySelectorAll(
      ".AddContractorToHandel"
    );
    addContractorButtons.forEach((button) => {
      button.addEventListener("click", function () {
        const contractorId = this.value;
        eel.GetContractorByID(contractorId)(function (data) {
          if (data && data.length > 0) {
            const contractorCode = data[0].Kod;
            selectContractor(contractorCode);
            window.location.href = "D_AddHandelDocument.html";
          } else {
            alert("Unable to find contractor.");
          }
        });
      });
    });
  });
});
