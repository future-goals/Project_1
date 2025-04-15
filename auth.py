import os

class User:
    def __init__(self,username,full_name,role):
     self.username = username
     self.full_name = full_name
     self.role= role

def authenticate(username, password):
    try:
        with open("data/password.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
    except FileNotFoundError:
        print("Error: password.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    
    return False

