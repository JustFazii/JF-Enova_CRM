import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIUpdateContractor:
    def request(self, data):
        add_kontrahent_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/UpdateContractor"
        session_token = GetSessionToken()

        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'application/json'
            }
            kontrahent_data = {
                "Kod": data['Kod'],
                "Nazwa": data['Nazwa'],
                "NIP": data['NIP'],
                "Adres": data['Adres'],
                "PodatnikVat": data['PodatnikVat'],
                "RodzajVatSprzedaz": data['RodzajVatSprzedaz'],
                "RodzajVatZakupu": data['RodzajVatZakupu'],
                "Status": data['Status'],
                "VatOd": data['VatOd'],
                "Ulica": data['Ulica'],
                "NrDomu": data['NrDomu'],
                "KodPoczt": data['KodPoczt'],
                "Poczta": data['Poczta'],
                "Woj": data['Woj'],
                "Miasto": data['Miasto'],
                "Kraj": data['Kraj']
            }
            service_response = requests.post(add_kontrahent_url, headers=service_headers, json=kontrahent_data)
            service_response.raise_for_status()
            data = service_response.json()
            
            return data
        
        except requests.exceptions.RequestException as e:
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            return f"Error: {ve}"
