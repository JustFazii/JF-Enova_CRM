import requests
from functions.env_file import TOKEN_ENOVA, IP
class APIShowHandelDocumentPositions:
    def __init__(self):
                self.base_token = TOKEN_ENOVA


    def send_request(self, param):
        login_url = f"http://{IP}:6001/api/LoginApi"
        pos_url = f"http://{IP}:6001/api/ServiceImpApiANS/GetPozycjeDokumentyHandlowe?value={param['value']}"

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
                raise ValueError("Nie udało się uzyskać tokenu sesji")

            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'text/json'
            }

            service_response = requests.post(pos_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()

            html_table = self.format_data(data)
            
            return html_table
        
        except requests.exceptions.RequestException as e:
            print(f"Błąd podczas komunikacji z API: {e}")
        except ValueError as ve:
            print(f"Błąd: {ve}")
        
    def format_data(self, data):
        html = "<table class='table-content'><thead><tr><th>Kod Towaru <span class='icon-arrow'>&uparrow;</span></th><th class='active asc'>Ilosc <span class='icon-arrow'>&uparrow;</span></th><th>Cena <span class='icon-arrow'>&uparrow;</span></th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls}'>{item['KodTowaru']}</td>"
                f"<td class='{cls} active'>{item['Ilosc']}</td>"
                f"<td class='{cls}'>{item['Cena']}</td>"
                f"</tr>"
            )
        html += "</table>"
        return html