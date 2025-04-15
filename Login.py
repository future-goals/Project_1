import tkinter as tk
from tkinter import messagebox
from tkinter import font
from auth import authenticate, get_user_details, add_user, delete_user

def login():
   username = username_entry.get()
   password = password_entry.get()

   role = authenticate(username, password)
   if role:
      user = get_user_details(username)
      if user:
         messagebox.showinfo("🌟 Login Successful", f"Welcome, {user.full_name}({user.role})!🥳")
         if role == "admin":
             admin_dashboard(user)
         elif role == "student":
             student_dashboard(user)
   else:
        messagebox.showerror("🚫 Login Failed", "Oops!! Try again.😥")

def admin_dashboard(user):
    """
    Admin Admin Dashboard
    """
    def add_user_ui():
        def submit():
            new_username = username_entry.get()
            new_full_name = new_full_name.get()
            new_password = password_entry.get()
            new_role = role_var.get()

            if add_user(new_username, new_password, new_full_name, new_role):
                messagebox.showinfo("✅ Success", "User added sucessfully!")
                add_user_window.destroy()
            else:
                messagebox.showerror("❌ Error", "Failed to add user 😵‍💫 Username might already exist.")

        add_user_window = tk.Toplevel()
        add_user_window.title("➕ Add User")
        add_user_window.geometry("400x350")

#----------------username----------------------------

        tk.Label(add_user_window, text="👤 Username:"). pack(pady=5)
        username_entry = tk.Entry(add_user_window)
        username_entry.pack(pady=5)

#-----------------full name---------------------------

        tk.Label(add_user_window, text="📛 Full Name:").pack(pady=5)
        full_name_entry = tk.Entry(add_user_window)
        full_name_entry.pack(pady=5)

#------------------password---------------------------

        tk.Label(add_user_window, text="🔑 Password:").pack(pady=5)
        password_entry = tk.Entry(add_user_window, show="*")
        password_entry.pack(pady=5)

#--------------------Role-----------------------------

        tk.Label(add_user, text="🧑‍🏫 Role:").pack(pady=5)
        role_var = tk.StringVar(value="Student")
        tk.OptionMenu(add_user_window, role_var, "admin", "student").pack(pady=5)

#---------------------Button--------------------------

        tk.Button(add_user_window, text="✅ Submit", command=submit).pack(pady=15)

    def delete_user_ui():
        def submit():
            username_to_delete = username_entry.get()
            if delete_user(username_to_delete):
               messagebox.showinfo("✅ Success", "User delted successfully!")
               delete_user_window.distroy()
            else:
                messagebox.showerror("❌ Error", "Failed to delete user. Username might exist.")

        delete_user_window = tk.Toplevel()
        delete_user_window.title("🗑️ Delete User")
        delete_user_window.geometry("300x200")

        tk.Label(delete_user_window, text="Username to delete:").pack(pady=10)
        username_entry = tk.Entry(delete_user_window)
        username_entry.pack(pady=10)

        tk.Button(delete_user_window, text="🗑️ Delete", command=submit).pack(pady=10)

    admin_window = tk.Toplevel()
    admin_window.title("⚙️ Admin Dashboard")
    admin_window.geometry("400x300")

#-------------------Header-------------------
    tk.Label(admin_window, text=f"👋 Welcome, {user.full_name}!", font=("Arial", 16, "bold")).pack(pady=15)

#------------------Button Frame---------------
    button_frame = tk.Frame(admin_window)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="➕ Add User", width=20, command=add_user_ui).pack(pady=5)
    tk.Button(button_frame, text="🗑️ Delete User", width=20, command=delete_user_ui).pack(pady=5)
    tk.Button(button_frame, text="🔙 Back / Exit", width=20, command=admin_window.destroy).pack(pady=20)


def student_dashboard(user):

    messagebox.showinfo("Student Dashboard", f"Welcome {user.full_name} 👔")

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

    title = tk.Label(root, text="Login", font=title_font, bg="#121212", fg="#00bfff")
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