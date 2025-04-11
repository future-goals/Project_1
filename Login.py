import tkinter as tk
from tkinter import messagebox
from tkinter import font

users = {
    "admin": "admin123",
    "unicorn": "rainbow",
    "pikachu": "thunderbolt"
}

def login():
   username = username_entry.get()
   password = password_entry.get()
   if username in users and users[username] == password:
        messagebox.showinfo("🌟 Login Successful", f"Welcome, {username}!🥳")
   else:
        messagebox.showerror("🚫 Login Failed", "Oops!! Try again.😥")

def toggle_password():
    if show_pass.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


def main():
    global username_entry, password_entry, show_pass

    root = tk.Tk()
    root.title("🌟 Login Portal 🌟")
    root.geometry("600x520")
    root.configure(bg="#121212")

    title_font = ("Consolas", 40, "bold")
    label_font = ("Consolas", 11)
    entry_font = ("Consolas", 11)

    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True)

    title = tk.Label(root, text="Welcom", font=title_font, bg="#121212", fg="#00bfff")
    title.pack(pady=(40, 20))

#--------------Username----------------

    tk.Label(root, text="Username:",font=label_font, bg="#121212", fg="#20c997").pack(pady=(10, 5))
    
    username_entry = tk.Entry(root, font=entry_font, justify="center", bg="#1e1e1e", relief="flat",fg="#ffffff", highlightthickness=2, highlightbackground="#20c997", highlightcolor="#00bfff", bd=2)
    username_entry.pack(ipady=7, ipadx=5, padx=50)

#--------------Password--------------------

    tk.Label(root, text="Password:",font=label_font, bg="#121212", fg="#20c997").pack(pady=(20, 5))
    
    password_entry = tk.Entry(root, show="*", font=entry_font, bg="#1e1e1e",fg="#ffffff", justify="center", relief="flat", highlightbackground="#20c997", highlightcolor="#00bfff", highlightthickness=2, bd=2)
    password_entry.pack(ipady=7, ipadx=5, padx=50)

#---------------Shoow-Password---------------

    show_pass = tk.BooleanVar()
    tk. Checkbutton(root, text="Show Password", variable=show_pass, command=toggle_password, bg="#121212", fg="#ffffff",relief="flat", activebackground="#121212", activeforeground="#ffffff", cursor="hand2").pack(pady=5)

#----------------Button------------------

    login_button = tk.Button(root, text="LOGIN", font=label_font, bg="#39ff14", fg="#121212", command=login, activebackground="#50ff50", activeforeground="#000000", relief="flat", bd=0, cursor="hand2")
    login_button.pack(pady=40, ipadx=20, ipady=10)

    login_button.configure(highlightbackground="#00bfff", highlightthickness=1)

    
    
    root.mainloop()


if __name__ == "__main__":
    main()