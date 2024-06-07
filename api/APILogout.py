import requests
from api.env_file import IP, PORT

class APILogout:
    def __init__(self, session_token):
        self.token = session_token

    def request(self):
        logout_url = f"http://{IP}:{PORT}/api/LogoutApi"

        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(logout_url, headers=headers)
            response.raise_for_status()
            logout_data = response.json()

            return logout_data
        
        except requests.exceptions.RequestException as e:
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"
