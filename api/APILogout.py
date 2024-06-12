import requests
from app.env_file import IP, PORT
from app.get_token import get_session_token

class APILogout:
    def request(self):
        logout_url = f"http://{IP}:{PORT}/api/LogoutApi"
        session_token = get_session_token()

        headers = {
            'Authorization': f'Bearer {session_token}',
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
