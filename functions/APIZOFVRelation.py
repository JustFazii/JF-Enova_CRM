import requests
from functions.env_file import TOKEN_ENOVA, IP
class APIZOFVRelation:
    def __init__(self):
                self.base_token = TOKEN_ENOVA


    def send_request(self, zofv):
        login_url = f"http://{IP}:6001/api/LoginApi"
        add_zofv_url = f"http://{IP}:6001/api/ServiceImpApiANS/TworzenieRelacjiZOFV?idDokumentuZO={zofv['idDokumentuZO']}"

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

            service_response = requests.post(add_zofv_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()
            
            return data
        
        except requests.exceptions.RequestException as e:
            return f"Błąd podczas komunikacji z API: {e}"
        except ValueError as ve:
            return f"Błąd: {ve}"