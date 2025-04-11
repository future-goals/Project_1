import os

class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self_role = role

def authenticate(username, password):
    try:
        with open("data/passwords.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) != 3:
                    print(f"Invalid line format: {line.strip()}")
                    continue
                stored_username, stored_password, role = fields
                if username == stored_username and password == stored_password:
                    return role
    except Exception as e:
        print(f"Authentication error: {e}")
    return None