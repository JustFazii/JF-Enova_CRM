class APPSetSettings:
    def setsettings(self, ip, port):
        env_vars = {
            "IP": ip,
            "PORT": port,
        }
        
        content = []
        try:
            with open('app/env_file.py', 'r') as file:
                content = file.readlines()
        except FileNotFoundError:
            print("env_file.py not found, creating a new one.")

        with open('app/env_file.py', 'w') as file:
            found_keys = {"IP": False, "PORT": False}
            for line in content:
                for key in env_vars:
                    if line.startswith(key):
                        file.write(f'{key} = "{env_vars[key]}"\n')
                        found_keys[key] = True
                        break
                else:
                    file.write(line)

            for key in env_vars:
                if not found_keys[key]:
                    file.write(f'{key} = "{env_vars[key]}"\n')
