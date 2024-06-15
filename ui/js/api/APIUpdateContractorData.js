document.addEventListener("DOMContentLoaded", function () {
  const contractorDataArray = JSON.parse(
    localStorage.getItem("contractorData")
  );
  if (contractorDataArray && contractorDataArray.length > 0) {
    const contractorData = contractorDataArray[0];
    document.getElementById("code").value = contractorData.Kod || "";
    document.getElementById("name").value = contractorData.Nazwa || "";
    document.getElementById("nip").value = contractorData.NIP || "";
    document.getElementById("adres").value = contractorData.Adres || "";
    document.getElementById("podvat").value = contractorData.PodatnikVat || "";
    document.getElementById("rodzvatsp").value =
      contractorData.RodzajVatSprzedaz || "";
    document.getElementById("rodzvatzk").value =
      contractorData.RodzajVatZakupu || "";
    document.getElementById("st-input").value = contractorData.Status || "";
    document.getElementById("vatod").value = contractorData.VatOd || "";
    document.getElementById("ulica").value = contractorData.Ulica || "";
    document.getElementById("nrdomu").value = contractorData.NrDomu || "";
    document.getElementById("kodpoczt").value = contractorData.KodPoczt || "";
    document.getElementById("poczta").value = contractorData.Poczta || "";
    document.getElementById("woj").value = contractorData.Woj || "";
    document.getElementById("miasto").value = contractorData.Miasto || "";
    document.getElementById("kraj").value = contractorData.Kraj || "";
  }
});
