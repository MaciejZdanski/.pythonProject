# 2FA Authentication System

A Python application that implements two-factor authentication (2FA) with a simple graphical user interface (GUI) using Tkinter.

## This project uses the following libraries:

    Tkinter for GUI
    pyotp for OTP generation

## Features
- User registration
- User login with password and OTP (One-Time Password)
- Password update
- User deletion (requires admin credentials)
- Passwords stored in plain text (for simplicity)

## Requirements
- Python 3.6 or higher
- Tkinter (for GUI)
- `pyotp` (for OTP generation)

## Installation
**1. Clone the repository:**

```bash
git clone https://github.com/yourusername/2fa-authentication-system.git
cd 2fa-authentication-system
```

**2. Install required packages:** 
 ```bash
 pip3 install pyotp
```
**3. Ensure Tkinter is installed:**
On Red Hat/CentOS:
 ```bash
 sudo yum install python3-tkinter
```
On Red Hat/CentOS:
 ```bash
 sudo yum install python3-tkinter
```
On Fedora:
 ```bash
sudo dnf install python3-tkinter
```

## Usage
**1. Run the application:**
```bash
python3 main.py
```
**2. Interacting with the GUI:**
-  **Register:** Enter a login and password, then click "Register" to create a new user.
- **Login:** Enter a login and password, then click "Login" to authenticate. An OTP will be displayed if successful.
- **Update Password:** Enter a login and new password, then click "Update Password" to change the user's password.
- **Delete User:** Enter a login, then click "Delete User". You will be prompted for admin credentials to confirm the deletion.

## File Structure

**1. main.py:** Main script to run the application with GUI.
**2. authentication_system.py:** Contains the AuthenticationSystem class for managing user authentication.
**3. user.py:** Contains the User class for managing user details.

## License

#### Creative Commons Attribution-NonCommercial 4.0 International License

**1. You are free to:**
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

**The licensor cannot revoke these freedoms as long as you follow the license terms.**

**2. Under the following terms:**
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- NonCommercial — You may not use the material for commercial purposes.

**3. No additional restrictions** 
You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

**4. Notices:**
- You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.
- No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.


## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
Acknowledgements

