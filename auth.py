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

def get_user_details(username):
    try:
        with open("data/user.txt","r")as file:
         for line in file:
          stored_username,full_name,role=line.strip().split(",")
        if username==stored_username:
         return User(username,full_name,role)
    except FileNotFoundError:
     print("Eror:user.txt file not found.")
    except Exception as e:
     print(f"Error:{e}")
    return None

def delete_user(username):
    try:
        # Delete from users.txt
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        with open("data/users.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ","):
                    file.write(line)

        # Delete from passwords.txt
        with open("data/passwords.txt", "r") as file:
            lines = file.readlines()
        with open("data/passwords.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ","):
                    file.write(line)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False