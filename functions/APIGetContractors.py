import requests

class APIGetContractors:
    def __init__(self):
        self.base_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdGgtbXRoIjoiMTAyNCIsImF0aC1wd3QiOiIxIiwiYXRoLWRiIjoiSU5GXzIyNDMyIiwiYXRoLWd1aWQiOiIzNmQ1NGRmYy04N2YyLTQ5YWEtYTRiMi1kM2FjZDhiZTY5YzYiLCJhdGgtc3ZjIjoiQXBpIiwibmJmIjoxNzE2NTU2NzY3LCJleHAiOjE3NDgwOTI3NjcsImlhdCI6MTcxNjU1Njc2NywiaXNzIjoiaHR0cHM6Ly93d3cuZW5vdmEucGwiLCJhdWQiOiJlbm92YTM2NSJ9.k4SbzPbPheoNn7CajBhWj0CzECeb5HzIEvSzahyeC3TaPiIcdxbnlijKZp2loe6JXu1z62V2pS4erLMpOBUUFrSnbet36iZpcXWGbL69VI3GCSHnwRcD1ssMYMxp6pKTZf0OdRfKlfyFeI4ntZdzh2vs7aBFhaHE0m5Wv3EpH3Biv9dVMACu6ayAthg4Of6vSMRfr7T_MZDN35aCYMsWordxlWUJwJ5K3YrpjfLAQXNLEsjfkv1dcqHY3NZtj2c1Z84PApRpIeo1kjJLvV5-7UIt7xX1cPMuC3omZfhEmUAuYe31YMHiLhb7QThx9Zcd33Tq0fYWPLe-pzVLelrthg"

    def send_request(self, param):
            login_url = "http://192.168.0.23:6001/api/LoginApi"
            service_url = "http://192.168.0.23:6001/api/ServiceImpApiANS/GetKontrahenci"

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
                    raise ValueError("Unable to access Session Token")

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
                print(f"Error while communicating with API: {e}")
                return f"Error while communicating with API: {e}"
            except ValueError as ve:
                print(f"Error: {ve}")
                return f"Error: {ve}"
            
    def format_data(self, data):
        html = "<table class='table-content'><thead><tr><th>ID</th><th>Kod</th><th>Nazwa</th><th>NIP</th><th>Adres</th></tr></thead>"
        for index, item in enumerate(data):
            cls = 'td-first' if index % 2 == 0 else 'td-second'
            html += (
                f"<tr>"
                f"<td class='{cls}'>{item['ID']}</td>"
                f"<td class='{cls}'>{item['Kod']}</td>"
                f"<td class='{cls}'>{item['Nazwa']}</td>"
                f"<td class='{cls}'>{item['NIP']}</td>"
                f"<td class='{cls}'>{item['Adres']}</td>"
                f"</tr>"
            )
        html += "</table>"
        return html