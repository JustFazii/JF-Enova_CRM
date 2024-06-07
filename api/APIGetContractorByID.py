import requests
from api.env_file import TOKEN_ENOVA, IP, PORT

class APIGetContractorByID:
    def __init__(self):
        self.token = TOKEN_ENOVA

    def request(self, id):
        login_url = f"http://{IP}:{PORT}/api/LoginApi"
        service_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetContractorByID?id={id}"

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
                raise ValueError("Unable to access Session Token")

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
            
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"