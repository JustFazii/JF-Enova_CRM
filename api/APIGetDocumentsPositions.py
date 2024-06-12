import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIGetDocumentsPositions:
    def request(self, param):
        document_position_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetDocumentsPositions?value={param}"
        session_token = GetSessionToken()
        
        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
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
        html = "<table class='table-content'><thead><tr><th>ID<span class='icon-arrow'>&uparrow;</span></th><th class='active asc'>Name<span class='icon-arrow'>&uparrow;</span></th><th>Value<span class='icon-arrow'>&uparrow;</span></th><th>Quantity<span class='icon-arrow'>&uparrow;</span></th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls}'>{item['TowarID']}</td>"
                f"<td class='{cls} active'>{item['NazwaTowaru']}</td>"
                f"<td class='{cls}'>{item['WartoscBrutto']}</td>"
                f"<td class='{cls}'>{item['Ilosc']} {item['Jednostka']}</td>"
                f"</tr>"
            )
        html += "</table>"
        return html