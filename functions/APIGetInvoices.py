import requests
from tabulate import tabulate
from functions.env_file import TOKEN_ENOVA, IP
class APIGetInvoices:
    def __init__(self):
                self.base_token = TOKEN_ENOVA

    def send_request(self, param):
        login_url = f"http://{IP}:6001/api/LoginApi"
        service_url = f"http://{IP}:6001/api/ServiceImpApiANS/GetFaktury"

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
                'Content-Type': 'application/json'
            }
            service_payload = {
                'param': param
            }
            service_response = requests.post(service_url, headers=service_headers, json=service_payload)
            service_response.raise_for_status()
            data = service_response.json()
            html_table = self.format_data(data)
            
            return html_table
            
        except requests.exceptions.RequestException as e:
            print(f"Błąd podczas komunikacji z API: {e}")
        except ValueError as ve:
            print(f"Błąd: {ve}")
            
    def format_data(self, data):
        html = "<table class='table-content'><thead><tr><th>ID <span class='icon-arrow'>&uparrow;</span></th><th class='active asc'>Definicja <span class='icon-arrow'>&uparrow;</span></th><th>Data <span class='icon-arrow'>&uparrow;</span></th><th>Kontrahent <span class='icon-arrow'>&uparrow;</span></th><th>Numer Dokumentu <span class='icon-arrow'>&uparrow;</span></th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls}'>{item['ID']}</td>"
                f"<td class='{cls} active'>{item['DefinicjaSymbol']}</td>"
                f"<td class='{cls}'>{item['Data']}</td>"
                f"<td class='{cls}'>{item['Kontrahent']}</td>"
                f"<td class='{cls}'>{item['NumerDokumentu']}</td>"
                f"</tr>"
            )
        html += "</table>"
        return html