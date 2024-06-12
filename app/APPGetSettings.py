class APPGetSettings():
    def getsettings(self):
        env_vars = {}
        try:
            with open('app/env_file.py', 'r') as file:
                content = file.readlines()
                for line in content:
                    if line.startswith(('IP', 'PORT', 'USER_TOKEN')):
                        key, value = line.split('=', 1)
                        env_vars[key.strip()] = value.strip().strip('"')
        except FileNotFoundError:
            print("env_file.py not found.")
        return env_vars