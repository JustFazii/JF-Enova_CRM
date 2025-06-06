import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIStatus:
    def request(self):
        service_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/APIStatus"
        session_token = GetSessionToken()

        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'application/json'
            }
            
            service_response = requests.post(service_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()
            
            if data == "Communication via API is Working!":
                data = "API: Connected"
            else:
                data = data
                
            return data
                
        except requests.exceptions.RequestException as e:
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            return f"Error: {ve}"