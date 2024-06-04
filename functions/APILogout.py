import requests

class EnovaApp:
    def __init__(self):
        self.base_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdGgtbXRoIjoiMjA0OCIsImF0aC1wd3QiOiIxIiwidW5pcXVlX25hbWUiOiJBZG1pbmlzdHJhdG9yIiwiYXRoLWRiIjoiSU5GXzIyNDMyIiwiYXRoLWd1aWQiOiIzNmQ1NGRmYy04N2YyLTQ5YWEtYTRiMi1kM2FjZDhiZTY5YzYiLCJhdGgtc3ZjIjoiQXBpIFNlcnZpY2VJbXBBcGlBTlMiLCJhdGgtaG5kIjoiTE9BRzVUVTBNbEtkVFMxWWk0d2kwSF9PZEpMc0lhSlk0U1hqS29Tc3o0cEFHIiwibmJmIjoxNzE3NDkxMzQwLCJleHAiOjE3MTc0OTE2NDAsImlhdCI6MTcxNzQ5MTM0MCwiaXNzIjoiaHR0cHM6Ly93d3cuZW5vdmEucGwiLCJhdWQiOiJlbm92YTM2NSJ9.kF4ou-DJmIJ8Usro8Ka2mgg1gBp0F9b27x--pYE5ZG1oaWZ17t8yCROJBcIvGfxYTkwnR8H0eQ7F2PLOsiR9QiIbgcn9a5oOkLMfD8cFv06Yxn88f9zHogv1eRP6ZhUiDE6o2fFo4AZ5g6KQormf4KYczEBMCW_u2WvwCOJ6qNN3mdKgTOqcwOKBWefP6awWTOz2dHsCoAxX4knNSMa153FJviIa8AAPyT01T6wgwEfE96dCmY_pYaEiZEtJ9wyS5-y6r5HiwsqCNXSCtZj3JN-4kWPklyo_Uyoo4vyFBldeBkKgFrl9Bf9geLNgvNKrrYl_tlPQRqP3cOm1__2gDA"

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
            session_token = logout_data.get('Token')

            # if not session_token:
            #     raise ValueError("Nie udało się uzyskać tokenu sesji")

            data = session_token
            print(response)
            print(data)
        except requests.exceptions.RequestException as e:
            print(f"Błąd podczas komunikacji z API: {e}")
        except ValueError as ve:
            print(f"Błąd: {ve}")

if __name__ == "__main__":
    app = EnovaApp()
    app.send_request()
