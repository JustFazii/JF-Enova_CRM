import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIAddHandelDocument:
    def request(self, data):
        service_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/AddHandelDocument"
        session_token = GetSessionToken()

        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'application/json'
            }

            service_data = {
                "Dokument": {
                    "Definicja": data['Definicja'],
                    "Data": "",
                    "Kontrahent": data['Kontrahent'],
                    "NumerDokumentu": ""
                },
                "Pozycje": data['Pozycje']
            }

            response = requests.post(service_url, headers=service_headers, json=service_data)
            response.raise_for_status()
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"