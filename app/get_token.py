def get_session_token():
    with open('app/env_file.py', 'r') as file:
        for line in file:
            if line.startswith('SESSION_TOKEN'):
                return line.split('=')[1].strip().strip('"')
    return None