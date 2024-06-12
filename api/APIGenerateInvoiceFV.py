import requests
from app.env_file import IP, PORT
from app.get_token import get_session_token

class APIGenerateInvoiceFV:
    def request(self, fv):
        add_fv_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GenerateInvoice?idDokumentuZO={fv['idDokumentuZO']}&typDokumentu=FV"
        session_token = get_session_token()

        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'text/json'
            }

            service_response = requests.post(add_fv_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()

            return data
        
        except requests.exceptions.RequestException as e:
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"