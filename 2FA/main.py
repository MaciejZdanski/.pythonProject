import tkinter as tk
from tkinter import simpledialog, messagebox
from authentication_system import AuthenticationSystem

ADMIN_LOGIN = "root"
ADMIN_PASSWORD = "toor"

def check_admin_credentials():
    admin_login = simpledialog.askstring("Admin Authentication", "Enter admin login:")
    admin_password = simpledialog.askstring("Admin Authentication", "Enter admin password:", show='*')
    return admin_login == ADMIN_LOGIN and admin_password == ADMIN_PASSWORD

def register_user():
    login = login_entry.get()
    password = password_entry.get()
    try:
        auth_system.register_user(login, password)
        messagebox.showinfo("Success", "User registered successfully")
    except ValueError:
        messagebox.showerror("Error", "User already exists")

def login_user():
    login = login_entry.get()
    password = password_entry.get()
    otp = auth_system.authenticate_user(login, password)
    if otp:
        messagebox.showinfo("OTP", f"Your OTP is: {otp}")
    else:
        messagebox.showerror("Error", "Invalid login or password")

def update_user_password():
    login = login_entry.get()
    new_password = password_entry.get()
    auth_system.update_password(login, new_password)
    messagebox.showinfo("Success", "Password updated successfully")

def delete_user():
    if not check_admin_credentials():
        messagebox.showerror("Error", "Invalid admin credentials")
        return

    login = login_entry.get()
    auth_system.delete_user(login)
    messagebox.showinfo("Success", "User deleted successfully")

auth_system = AuthenticationSystem("baza.json")

root = tk.Tk()
root.title("2FA Authentication System")

login_label = tk.Label(root, text="Login:")
login_label.grid(row=0, column=0)
login_entry = tk.Entry(root)
login_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=2, column=0)

login_button = tk.Button(root, text="Login", command=login_user)
login_button.grid(row=2, column=1)

update_button = tk.Button(root, text="Update Password", command=update_user_password)
update_button.grid(row=3, column=0)

delete_button = tk.Button(root, text="Delete User", command=delete_user)
delete_button.grid(row=3, column=1)

root.mainloop()
