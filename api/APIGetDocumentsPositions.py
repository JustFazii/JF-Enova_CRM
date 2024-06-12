import requests
from app.env_file import IP, PORT, SESSION_TOKEN

class APIGetDocumentsPositions:
    def request(self, param):
        document_position_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetDocumentsPositions?value={param['value']}"

        try:
            service_headers = {
                'Authorization': f'Bearer {SESSION_TOKEN}',
                'Content-Type': 'text/json'
            }

            service_response = requests.post(document_position_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()

            html_table = self.format_data(data)
            
            return html_table
        
        except requests.exceptions.RequestException as e:
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"
        
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