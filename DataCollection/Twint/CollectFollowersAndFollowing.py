import twint
import json

users_file_path = ''

# Load users

with open(users_file_path, 'r') as f:
    for line in f:
        user = json.loads(line)
        print(user)