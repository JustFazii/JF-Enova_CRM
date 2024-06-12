import requests
from app.env_file import IP, PORT, SESSION_TOKEN

class APIPassEcho:
    def request(self, string):
        echo_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/PassEcho"

        try:
            service_headers = {
                'Authorization': f'Bearer {SESSION_TOKEN}',
                'Content-Type': 'text/json'
            }
            params = {
                'value': string
            }
            service_response = requests.post(echo_url, headers=service_headers, params=params)
            service_response.raise_for_status()
            data = service_response.json()
            
            print(data)
            
            return data
        
        except requests.exceptions.RequestException as e:
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"
