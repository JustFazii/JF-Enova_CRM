import requests
from api.env_file import TOKEN_ENOVA, IP, PORT

class APIGetGoods:
    def __init__(self):
        self.token = TOKEN_ENOVA

    def request(self):
        login_url = f"http://{IP}:{PORT}/api/LoginApi"
        goods_url = f"http://{IP}:{PORT}/api/ServiceImpApiANS/GetGoods"

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
                raise ValueError("Nie udało się uzyskać tokenu sesji")

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
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"

    def format_data(self, data):
        html = "<table class='table-content'><thead><tr><th class='active asc'>Code <span class='icon-arrow'>&uparrow;</span></th><th>Name <span class='icon-arrow'>&uparrow;</span></th><th>Price <span class='icon-arrow'>&uparrow;</span></th><th>Availability <span class='icon-arrow'>&uparrow;</span></th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls} active'>{item['Kod']}</td>"
                f"<td class='{cls}'>{item['Nazwa']}</td>"
                f"<td class='{cls}'>{str(item['Cena']) + ' ' + item['Waluta']}</td>"
                f"<td class='{cls}'>{item['IloscDostepna']}</td>"
                f"</tr>"
            )
        html += "</table>"
        return html