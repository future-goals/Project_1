import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def main():
    root = tk.Tk()
    root.title("User View")
    root.geometry("600x600")

    frame = tk.Frame(root)
    frame.pack(expand=True)


    tk.Label(frame, text="Username:").pack(pady=5)
    global username_entry
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)


    tk.Label(frame, text="Password:").pack(pady=5)
    global password_entry
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=5)


    tk.Button(frame, text="Login", command=login).pack(pady=10)


    root.mainloop()


if __name__ == "__main__":
    main()