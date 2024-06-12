import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIGetContractors:
    def request(self):
        service_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetContractors"
        session_token = GetSessionToken()
        
        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'application/json'
            }
            
            service_response = requests.post(service_url, headers=service_headers)
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
        html = "<table class='table-content'><thead><tr><th>ID <span class='icon-arrow'>&uparrow;</span></th><th class='active asc'>Code <span class='icon-arrow'>&uparrow;</span></th><th>Name <span class='icon-arrow'>&uparrow;</span></th><th>NIP <span class='icon-arrow'>&uparrow;</span></th><th>Address <span class='icon-arrow'>&uparrow;</span></th><th>Options</th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls}'>{item['ID']}</td>"
                f"<td class='{cls} active'>{item['Kod']}</td>"
                f"<td class='{cls}'>{item['Nazwa']}</td>"
                f"<td class='{cls}'>{item['NIP']}</td>"
                f"<td class='{cls}'>{item['Adres']}</td>"
                f"<td class='{cls}'><div class='Buttons'><button class='ShowContractorButton' value={item['ID']} title='Show documents positions'><i class='icon ph-bold ph-user-gear'></i></button></div></td>"
                f"</tr>"
            )
        html += "</table>"
        return html