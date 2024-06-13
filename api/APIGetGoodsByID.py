import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIGetGoodsByID:
    def request(self, id):
        service_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetGoodByID?id={id}"
        session_token = GetSessionToken()

        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'accept': 'application/json'
            }
            
            params = {
            'id': id
            }
            
            service_response = requests.post(service_url, headers=service_headers, params=params)
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