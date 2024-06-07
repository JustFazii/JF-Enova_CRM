import requests
from api.env_file import TOKEN_ENOVA, IP, PORT

class APIUpdateContractor:
    def __init__(self):
        self.token = TOKEN_ENOVA

    def request(self, data):
        login_url = f"http://{IP}:{PORT}/api/LoginApi"
        add_kontrahent_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/UpdateContractor"

        headers = {
            'Authorization': f'Bearer {self.token}',
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
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"
