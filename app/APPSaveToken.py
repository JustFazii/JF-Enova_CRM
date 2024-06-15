import re

def SaveTokens(user_token, session_token):
    env_file = 'app/env_file.py'
    
    with open(env_file, 'r') as file:
        content = file.read()
    
    if 'USER_TOKEN' in content:
        content = re.sub(r'USER_TOKEN\s*=\s*".*"', f'USER_TOKEN = "{user_token}"', content)
    else:
        content += f'\nUSER_TOKEN = "{user_token}"\n'
    
    if 'SESSION_TOKEN' in content:
        content = re.sub(r'SESSION_TOKEN\s*=\s*".*"', f'SESSION_TOKEN = "{session_token}"', content)
    else:
        content += f'\nSESSION_TOKEN = "{session_token}"\n'
    
    with open(env_file, 'w') as file:
        file.write(content)
