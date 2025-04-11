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
    root.geometry("400x320")
    root.configure(bg="#FFFDF2")

    frame = tk.Frame(root, bg="#FFFDF2")
    frame.pack(expand=True)

    title = tk.Label(frame, text="Welcome", font=("Comic Sans MS", 22, "bold"), bg="#FFFDF2", fg="#000000")
    title.pack(pady=15)

    tk.Label(frame, text="Username:", bg="#FFFDF2").pack()
    global username_entry
    username_entry = tk.Entry(frame, font=("Arial", 12), justify="center", bg="#ffffff", relief="groove", bd=2)
    username_entry.pack(pady=5)

    tk.Label(frame, text="Password:", bg="#FFFDF2").pack()
    global password_entry
    password_entry = tk.Entry(frame, show="*", font=("Arial", 12), justify="center", bg="#ffffff", relief="groove", bd=2)
    password_entry.pack(pady=5)

    login_button = tk.Button(frame, text="Log In", font=("Arial", 12, "bold"), bg="#b19cd9", fg="white", command=login)
    login_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
