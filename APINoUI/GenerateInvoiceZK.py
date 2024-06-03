import requests
from tabulate import tabulate

class EnovaApp:
    def __init__(self):
        self.base_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdGgtbXRoIjoiMTAyNCIsImF0aC1wd3QiOiIxIiwiYXRoLWRiIjoiSU5GXzIyNDMyIiwiYXRoLWd1aWQiOiIzNmQ1NGRmYy04N2YyLTQ5YWEtYTRiMi1kM2FjZDhiZTY5YzYiLCJhdGgtc3ZjIjoiQXBpIiwibmJmIjoxNzE2NTU2NzY3LCJleHAiOjE3NDgwOTI3NjcsImlhdCI6MTcxNjU1Njc2NywiaXNzIjoiaHR0cHM6Ly93d3cuZW5vdmEucGwiLCJhdWQiOiJlbm92YTM2NSJ9.k4SbzPbPheoNn7CajBhWj0CzECeb5HzIEvSzahyeC3TaPiIcdxbnlijKZp2loe6JXu1z62V2pS4erLMpOBUUFrSnbet36iZpcXWGbL69VI3GCSHnwRcD1ssMYMxp6pKTZf0OdRfKlfyFeI4ntZdzh2vs7aBFhaHE0m5Wv3EpH3Biv9dVMACu6ayAthg4Of6vSMRfr7T_MZDN35aCYMsWordxlWUJwJ5K3YrpjfLAQXNLEsjfkv1dcqHY3NZtj2c1Z84PApRpIeo1kjJLvV5-7UIt7xX1cPMuC3omZfhEmUAuYe31YMHiLhb7QThx9Zcd33Tq0fYWPLe-pzVLelrthg"


    def send_request(self, zdzk):
        login_url = "http://192.168.0.23:6001/api/LoginApi"
        add_zdzk_url = f"http://192.168.0.23:6001/api/ServiceImpApiANS/GenerateInvoice?idDokumentuZO={zdzk['value']}&typDokumentu=ZK"

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

            service_response = requests.post(add_zdzk_url, headers=service_headers)
            service_response.raise_for_status()
            data = service_response.json()
            
            print(data)
            
        except requests.exceptions.RequestException as e:
            print(f"Błąd podczas komunikacji z API: {e}")
        except ValueError as ve:
            print(f"Błąd: {ve}")
            
    def format_data(self, data):
        table = []
        for item in data:
            table.append([item['KodTowaru'], item['Ilosc'], item['Cena']])
        return tabulate(table, headers=["KodTowaru", "Ilosc", "Cena"], tablefmt="grid")

if __name__ == "__main__":
    app = EnovaApp()
    zdzk = {
        "value": "4",
    }
    app.send_request(zdzk)
