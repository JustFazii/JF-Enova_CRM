import requests
from functions.env_file import TOKEN_ENOVA, IP
class APIUpdateStatus:
    def __init__(self):
                self.base_token = TOKEN_ENOVA
    
    def send_request(self, param):
        login_url = f"http://{IP}:6001/api/LoginApi"
        service_url = f"http://{IP}:6001/api/ServiceImpApiANS/TestApi"

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
                raise ValueError("Unable to access Session Token")

            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'application/json'
            }
            service_payload = {
                'param': param
            }
            service_response = requests.post(service_url, headers=service_headers, json=service_payload)
            service_response.raise_for_status()
            
            data = service_response.json()
            
            if data == "Komunikacja z WebAPI enova działa!":
                display_message = "Connected"
            else:
                display_message = "Disconnected"
            
            return display_message
            
        
        except requests.exceptions.HTTPError as http_err:
            if http_err.response.status_code == 401:
                print(f"Błąd 401: Unauthorized - {http_err}")
                return "Disconnected - Unauthorized"
        except requests.exceptions.RequestException as e:
             print(f"Error while communicating with API: {e}")
             api = "API Error"
             return api
        except ValueError as ve:
             api = f"Error: {ve}"
             return api