import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIPassEcho:
    def request(self, string):
        echo_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/PassEcho"
        session_token = GetSessionToken()

        try:
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
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            return f"Error: {ve}"
