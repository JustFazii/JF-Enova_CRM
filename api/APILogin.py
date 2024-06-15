import requests
from app.APPSaveToken import SaveTokens
from app.APPGetSettingsPort import GetSettingsPort
from app.APPGetSettingsIP import GetSettingsIP

class APILogin:
    def request(self, user_token):
        IP = GetSettingsIP()
        PORT = GetSettingsPort()
        
        print(IP, PORT)
        
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
            print(f"Error when connecting with API: {e}")
            return f"Error while communicating with API: {e}"
        except ValueError as ve:
            print(f"Error: {ve}")
            return f"Error: {ve}"
