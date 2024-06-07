import requests
from api.env_file import TOKEN_ENOVA, IP, PORT

class APIPassEcho:
    def __init__(self):
        self.token = TOKEN_ENOVA

    def request(self, string):
        login_url = f"http://{IP}:{PORT}/api/LoginApi"
        echo_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetEcho"

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
                'Content-Type': 'text/json'
            }
            params = {
                'value': string
            }
            service_response = requests.post(echo_url, headers=service_headers, params=params)
            service_response.raise_for_status()
            data = service_response.json()
            
            return data
        
        except requests.exceptions.RequestException as e:
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"
