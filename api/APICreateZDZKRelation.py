import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APICreateZDZKRelation:
    def request(self, id):
        zdzk_relation_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/CreateZDZKRelation?idDokumentuZD={id}"
        session_token = GetSessionToken()

        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'text/json'
            }

            service_response = requests.post(zdzk_relation_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()

            return data
        
        except requests.exceptions.RequestException as e:
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            return f"Error: {ve}"
