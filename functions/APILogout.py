import requests

class APILogout:
    def __init__(self):
        self.base_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdGgtbXRoIjoiMjA0OCIsImF0aC1wd3QiOiIxIiwidW5pcXVlX25hbWUiOiJBZG1pbmlzdHJhdG9yIiwiYXRoLWRiIjoiSU5GXzIyNDMyIiwiYXRoLWd1aWQiOiIzNmQ1NGRmYy04N2YyLTQ5YWEtYTRiMi1kM2FjZDhiZTY5YzYiLCJhdGgtc3ZjIjoiQXBpIFNlcnZpY2VJbXBBcGlBTlMiLCJhdGgtaG5kIjoiVWdIVzJoQWFEWURMM0UwV3RweDdDRV9JTGYxMGFnUXVGNGdub0FVcFpCZTBHIiwibmJmIjoxNzE3NDkxNzEwLCJleHAiOjE3MTc0OTIwMTAsImlhdCI6MTcxNzQ5MTcxMCwiaXNzIjoiaHR0cHM6Ly93d3cuZW5vdmEucGwiLCJhdWQiOiJlbm92YTM2NSJ9.XQcjEabNytpZWuTWrcabvv1ShezVzVNpHvaMTd_guECf28YF1F7DGGqdBXm0_HuBiIFNWk5eYVxReLe70poJShuf4VBayrTRCcHjHArrwQxYDVl4aIEjT0TeUr4AB_ep98BFtyLe3-4B92vCBUZ9vOScTWKocrN6FDhZ85In3xQ4bxazbsG6FmmsRtcCbOjdZcpiEWUjppc-Hh8rxi1e49Kcem7XD2buWT_860RybUI-wykIEU79-KgTcE7798BRD40mznT8-lY1Gmh9S6KBFxrSklFgBv0DxmWyhAO6gA0Er9-Egb8Mv5oZswyfvKzq16cwCHE2hELSFR15Szy2qw"

    def send_request(self):
        logout_url = "http://192.168.0.23:6001/api/LogoutApi"

        headers = {
            'Authorization': f'Bearer {self.base_token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(logout_url, headers=headers)
            response.raise_for_status()
            logout_data = response.json()
            responseAPI = logout_data.get('LoggedOut')
            
            print(responseAPI)
            
        except requests.exceptions.RequestException as e:
            print(f"Błąd podczas komunikacji z API: {e}")
        except ValueError as ve:
            print(f"Błąd: {ve}")

if __name__ == "__main__":
    app = APILogout()
    app.send_request()
