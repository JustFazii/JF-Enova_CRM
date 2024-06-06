import requests
from functions.env_file import TOKEN_ENOVA, IP

class APIAddContractor:
    def __init__(self):
        self.base_token = TOKEN_ENOVA


    def send_request(self, kontrahent):
        print("Sending request with data:", kontrahent)
        login_url = f"http://{IP}:6001/api/LoginApi"
        add_kontrahent_url = f"http://{IP}:6001/api/ServiceImpApiANS/AddKontrahent"

        headers = {
            'Authorization': f'Bearer {self.base_token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(login_url, headers=headers)
            response.raise_for_status()
            login_data = response.json()
            session_token = login_data.get('Token')

            if not session_token:
                raise ValueError("Nie udało się uzyskać tokenu sesji")

            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'application/json'
            }
            kontrahent_data = {
                "Kod": kontrahent['Kod'],
                "Nazwa": kontrahent['Nazwa'],
                "NIP": kontrahent['NIP'],
                "Adres": kontrahent['Adres'],
                "PodatnikVat": kontrahent['PodatnikVat'],
                "RodzajVatSprzedaz": kontrahent['RodzajVatSprzedaz'],
                "RodzajVatZakupu": kontrahent['RodzajVatZakupu'],
                "Status": kontrahent['Status'],
                "VatOd": kontrahent['VatOd'],
                "Ulica": kontrahent['Ulica'],
                "NrDomu": kontrahent['NrDomu'],
                "KodPoczt": kontrahent['KodPoczt'],
                "Poczta": kontrahent['Poczta'],
                "Woj": kontrahent['Woj'],
                "Miasto": kontrahent['Miasto'],
                "Kraj": kontrahent['Kraj']
            }
            print(kontrahent_data)
            service_response = requests.post(add_kontrahent_url, headers=service_headers, json=kontrahent_data)
            service_response.raise_for_status()
            data = service_response.json()
            
            return data
        
        except requests.exceptions.RequestException as e:
            print(f"Błąd podczas komunikacji z API: {e}")
            return {"error": str(e)}
        except ValueError as ve:
            print(f"Błąd: {ve}")
            return {"error": str(ve)}
