import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "password":
        messagebox.showinfo("🌟 Login Successful", f"Welcome, {username}!🥳")
    else:
        messagebox.showerror("🚫 Login Failed", "Oops!! Try again.😥")


def main():
    root = tk.Tk()
    root.title("🌟 Login Portal 🌟")
    root.geometry("400x300")
    root.configure(bg="#FFFDF2")

    title = tk.Label(root, text="✨ Welcome!", font=("Style Script", 18, "bold"), bg="#FFFDF2", fg="#000000")
    title.pack(pady=15)

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