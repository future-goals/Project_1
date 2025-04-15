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
                fields = line.strip().split(",")
                if len(fields) != 3:
                   print(f"Invalide line format in password.txt:{line.strip()}")
                   continue
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
        
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        with open("data/users.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ","):
                    file.write(line)

        
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
    
def get_student_grades(username):
    try:
        with open("data/grades.txt", "r") as file:
            for line in file:
                stored_username, *grades = line.strip().split(",")
                if username == stored_username:
                    return grades
    except FileNotFoundError:
        print("Error: grades.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_student_eca(username):
    try:
        with open("data/eca.txt", "r") as file:
            for line in file:
                stored_username, *activities = line.strip().split(",")
                if username == stored_username:
                    return activities
    except FileNotFoundError:
        print("Error: eca.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def update_student_profile(username, full_name):
    try:
        updated = False
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        with open("data/users.txt", "w") as file:
            for line in lines:
                stored_username, _, role = line.strip().split(",")
                if username == stored_username:
                    file.write(f"{username},{full_name},{role}\n")
                    updated = True
                else:
                    file.write(line)
        return updated
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return False
