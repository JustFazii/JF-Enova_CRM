import requests
from app.env_file import IP, PORT
from app.APPGetToken import GetSessionToken

class APIGetGoods:
    def request(self):
        goods_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetGoods"
        session_token = GetSessionToken()

        try:
            service_headers = {
                'Authorization': f'Bearer {session_token}',
                'Content-Type': 'application/json'
            }

            service_response = requests.post(goods_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()
            formatted_data = self.format_data(data)
            
            return formatted_data
        
        except requests.exceptions.RequestException as e:
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            return f"Error: {ve}"

    def format_data(self, data):
        html = "<table class='table-content'><thead><tr><th>ID<span class='icon-arrow'>&uparrow;</span></th><th class='active asc'>Code<span class='icon-arrow'>&uparrow;</span></th><th>Name<span class='icon-arrow'>&uparrow;</span></th><th>Price<span class='icon-arrow'>&uparrow;</span></th><th>Availability<span class='icon-arrow'>&uparrow;</span></th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls}'>{item['ID']}</td>"
                f"<td class='{cls} active'>{item['Kod']}</td>"
                f"<td class='{cls}'>{item['Nazwa']}</td>"
                f"<td class='{cls}'>{str(item['Cena']) + ' ' + item['Waluta']}</td>"
                f"<td class='{cls}'>{item['IloscDostepna']}</td>"
                f"</tr>"
            )
        html += "</table>"
        return html