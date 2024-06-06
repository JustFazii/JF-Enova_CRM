import requests
from functions.env_file import TOKEN_ENOVA, IP
class APIGetEcho:
    def __init__(self):
                self.base_token = TOKEN_ENOVA

    def send_request(self, param):
        login_url = f"http://{IP}:6001/api/LoginApi"
        service_url = f"http://{IP}:6001/api/ServiceImpApiANS/GetEcho"

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
                'Content-Type': 'text/json'
            }
            params = {
                'value': param
            }
            service_response = requests.post(service_url, headers=service_headers, params=params)
            service_response.raise_for_status()
            data = service_response.json()
            
            return data
        
        except requests.exceptions.RequestException as e:
            return f"Błąd podczas komunikacji z API: {e}"
        except ValueError as ve:
            return f"Błąd: {ve}"
