document
  .getElementById("submit-btn-up")
  .addEventListener("click", function (event) {
    event.preventDefault();
    const contractorData = {
      Kod: document.getElementById("code").value,
      Nazwa: document.getElementById("name").value,
      NIP: document.getElementById("nip").value,
      Adres: document.getElementById("adres").value,
      PodatnikVat: document.getElementById("podvat").value,
      RodzajVatSprzedaz: document.getElementById("rodzvatsp").value,
      RodzajVatZakupu: document.getElementById("rodzvatzk").value,
      Status: document.getElementById("st-input").value,
      VatOd: document.getElementById("vatod").value,
      Ulica: document.getElementById("ulica").value,
      NrDomu: document.getElementById("nrdomu").value,
      KodPoczt: document.getElementById("kodpoczt").value,
      Poczta: document.getElementById("poczta").value,
      Woj: document.getElementById("woj").value,
      Miasto: document.getElementById("miasto").value,
      Kraj: document.getElementById("kraj").value,
    };

    eel.UpdateContractor(contractorData)(function (data) {
      document.getElementById("get-contup-response").innerText = data;

      setTimeout(function () {
        window.location.href = "C_Contractors.html";
      }, 3000);
    });
  });
