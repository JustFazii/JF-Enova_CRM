import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIGenerateInvoiceZK:
    def request(self, zk):
        add_zk_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GenerateInvoice?idDokumentuZD={zk['idDokumentuZD']}&typDokumentu=ZK"
        session_token = GetSessionToken()

        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'text/json'
            }

            service_response = requests.post(add_zk_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()

            return data
        
        except requests.exceptions.RequestException as e:
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            return f"Error: {ve}"