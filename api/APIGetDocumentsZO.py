import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIGetZODocuments:
    def request(self):
        zo_documents_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetZODocuments"
        session_token = GetSessionToken()

        try:
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
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            return f"Error: {ve}"
            
    def format_data(self, data):
        html = "<table class='table-content'><thead><tr><th>ID<span class='icon-arrow'>&uparrow;</span></th><th class='active asc'>Definition<span class='icon-arrow'>&uparrow;</span></th><th>Document Nr.<span class='icon-arrow'>&uparrow;</span></th><th>Date<span class='icon-arrow'>&uparrow;</span></th><th>Contractor ID<span class='icon-arrow'>&uparrow;</span></th><th>Contractor<span class='icon-arrow'>&uparrow;</span></th><th>Value<span class='icon-arrow'>&uparrow;</span></th><th>Options</th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls}'>{item['ID']}</td>"
                f"<td class='{cls} active'>{item['DefinicjaSymbol']}</td>"
                f"<td class='{cls}'>{item['NumerDokumentu']}</td>"
                f"<td class='{cls}'>{item['DataDok']}</td>"
                f"<td class='{cls}'>{item['KontrahentID']}</td>"
                f"<td class='{cls}'>{item['KontrahentNazwa']}</td>"
                f"<td class='{cls}'>{item['WartoscBrutto']}</td>"
                f"<td class='{cls}'><div class='Buttons'><Button class='ShowPosButton' value={item['ID']} title='Show documents positions'><i class='icon ph-bold ph-file-lock'></i></Button><Button class='ShowRelationButton' value={item['ID']} title='Add relation with FV document'><i class='icon ph-bold ph-folder-lock'></i></Button></div></td>"
                f"</tr>"
            )
        html += "</table>"
        return html