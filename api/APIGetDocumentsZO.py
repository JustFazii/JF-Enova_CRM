import requests
from api.env_file import TOKEN_ENOVA, IP, PORT

class APIGetZODocuments:
    def __init__(self):
        self.token = TOKEN_ENOVA

    def request(self):
        login_url = f"http://{IP}:{PORT}/api/LoginApi"
        zo_documents_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetZODocuments"

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
                'Content-Type': 'application/json'
            }
            
            service_response = requests.post(zo_documents_url, headers=service_headers)
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
        html = "<table class='table-content'><thead><tr><th>ID<span class='icon-arrow'>&uparrow;</span></th><th class='active asc'>Definition<span class='icon-arrow'>&uparrow;</span></th><th>Date<span class='icon-arrow'>&uparrow;</span></th><th>Contractor<span class='icon-arrow'>&uparrow;</span></th><th>Document Number<span class='icon-arrow'>&uparrow;</span></th><th>Options</th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls}'>{item['ID']}</td>"
                f"<td class='{cls} active'>{item['DefinicjaSymbol']}</td>"
                f"<td class='{cls}'>{item['Data']}</td>"
                f"<td class='{cls}'>{item['Kontrahent']}</td>"
                f"<td class='{cls}'>{item['NumerDokumentu']}</td>"
                f"<td class='{cls}'><div class='Buttons'><Button class='ShowPosButton' value={item['ID']} title='Show documents positions'><i class='icon ph-bold ph-file-lock'></i></Button><Button class='ShowPosButton' value={item['ID']} title='Add relation with FV document'><i class='icon ph-bold ph-folder-lock'></i></Button></div></td>"
                f"</tr>"
            )
        html += "</table>"
        return html