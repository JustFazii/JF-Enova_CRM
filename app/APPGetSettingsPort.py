def GetSettingsPort():
    with open('app/env_file.py', 'r') as file:
        for line in file:
            if line.startswith('Port'):
                return line.split('=')[1].strip().strip('"')
    return None