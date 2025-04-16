import os
from pathlib import Path

class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role

def ensure_data_directory():
    """Ensure the data directory exists"""
    Path("data").mkdir(exist_ok=True)

def authenticate(username, password):
    try:
        ensure_data_directory()
        with open("data/password.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) != 3:
                    continue  # Skip malformed lines
                stored_username, stored_password, _ = fields
                if username == stored_username and password == stored_password:
                    return True
    except FileNotFoundError:
        print("Error: password.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return False

def get_user_details(username):
    try:
        ensure_data_directory()
        with open("data/users.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) != 3:
                    continue
                stored_username, full_name, role = fields
                if username == stored_username:
                    return User(username, full_name, role)
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def add_user(username, full_name, password, role):
    try:
        ensure_data_directory()
        
        # Check if user exists in either file
        user_exists = False
        if os.path.exists("data/users.txt"):
            with open("data/users.txt", "r") as file:
                for line in file:
                    stored_username, _, _ = line.strip().split(",")
                    if username == stored_username:
                        user_exists = True
                        break
        
        if user_exists:
            return False

        # Add to users file
        with open("data/users.txt", "a") as file:
            file.write(f"{username},{full_name},{role}\n")

        # Add to password file
        with open("data/password.txt", "a") as file:
            file.write(f"{username},{password},{role}\n")

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def delete_user(username):
    try:
        ensure_data_directory()
        deleted = False
        
        # Delete from users file
        if os.path.exists("data/users.txt"):
            with open("data/users.txt", "r") as file:
                lines = file.readlines()
            with open("data/users.txt", "w") as file:
                for line in lines:
                    if not line.startswith(username + ","):
                        file.write(line)
                    else:
                        deleted = True

        # Delete from password file
        if os.path.exists("data/password.txt"):
            with open("data/password.txt", "r") as file:
                lines = file.readlines()
            with open("data/password.txt", "w") as file:
                for line in lines:
                    if not line.startswith(username + ","):
                        file.write(line)

        return deleted
    except Exception as e:
        print(f"Error: {e}")
        return False

def get_student_grades(username):
    try:
        ensure_data_directory()
        if not os.path.exists("data/grades.txt"):
            return None
            
        with open("data/grades.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if not fields:
                    continue
                stored_username = fields[0]
                if username == stored_username:
                    return fields[1:]  # Return all grades
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_student_eca(username):
    try:
        ensure_data_directory()
        if not os.path.exists("data/eca.txt"):
            return None
            
        with open("data/eca.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if not fields:
                    continue
                stored_username = fields[0]
                if username == stored_username:
                    return fields[1:]  # Return all activities
    except Exception as e:
        print(f"Error: {e}")
    return None

def update_student_profile(username, full_name):
    try:
        ensure_data_directory()
        if not os.path.exists("data/users.txt"):
            return False
            
        updated = False
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
            
        with open("data/users.txt", "w") as file:
            for line in lines:
                fields = line.strip().split(",")
                if len(fields) != 3:
                    file.write(line)  # Keep malformed lines as-is
                    continue
                    
                stored_username, _, role = fields
                if username == stored_username:
                    file.write(f"{username},{full_name},{role}\n")
                    updated = True
                else:
                    file.write(line)
                    
        return updated
    except Exception as e:
        print(f"Error: {e}")
        return False
