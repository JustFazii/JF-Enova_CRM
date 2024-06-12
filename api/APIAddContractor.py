import requests
from app.env_file import IP, PORT
from app.get_token import get_session_token

class APIAddContractor:
    def request(self, data):
        add_contractor_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/AddContractor"
        session_token = get_session_token()

        try:

            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'application/json'
            }
            kontrahent_data = {
                "Kod": data['Kod'],
                "Nazwa": data['Nazwa'],
                "NIP": data['NIP'],
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
            
            service_response = requests.post(add_contractor_url, headers=service_headers, json=kontrahent_data)
            service_response.raise_for_status()
            data = service_response.json()
            
            return data
        
        except requests.exceptions.RequestException as e:
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"
