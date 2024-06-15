import requests
from app.env_file import IP, PORT
from app.APPSaveToken import SaveTokens

class APIRefreshToken:
    def request(self, user_token):
        login_url = f"http://{IP}:{PORT}/api/LoginApi"

        headers = {
            'Authorization': f'Bearer {user_token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(login_url, headers=headers)
            response.raise_for_status()
            login_data = response.json()
            session_token = login_data.get('Token')

            if not session_token:
                raise ValueError("Nie udało się uzyskać tokenu sesji")

            SaveTokens(user_token, session_token)

            return session_token
        
        except requests.exceptions.RequestException as e:
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            return f"Error: {ve}"
