import json

def extract_usernames_from_config(config_file, log_file):
    try:
        with open(config_file, 'r') as f:
            data = json.load(f)
            usernames = [entry['username'] for entry in data]
            with open(log_file, 'w') as log:
                for username in usernames:
                    log.write(username + '\n')
            print(f"Usernames extracted from '{config_file}' and saved to '{log_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{config_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{config_file}'.")

if __name__ == "__main__":
    config_file = "config.json"
    log_file = "extracted_usernames.ini"
    extract_usernames_from_config(config_file, log_file)
