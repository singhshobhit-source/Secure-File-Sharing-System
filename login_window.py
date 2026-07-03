import tkinter as tk
from tkinter import messagebox
from auth import register_user, login_user


def open_login():

    root = tk.Tk()

    root.title("Secure File Sharing System")
    root.geometry("500x650")
    root.configure(bg="#1e1e2f")
    root.resizable(False, False)

    # Register function
    def register():

        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please enter username and password"
            )
            return

        register_user(username, password)

        messagebox.showinfo(
            "Success",
            "Registration completed successfully!"
        )

    # Login function
    def login():

        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please enter username and password"
            )
            return

        success = login_user(username, password)

        if success:

            messagebox.showinfo(
                "Success",
                "Login successful!"
            )

            root.destroy()

            # Import here to avoid circular import
            from dashboard import open_dashboard
            open_dashboard()

        else:

            messagebox.showerror(
                "Error",
                "Invalid username or password"
            )

    # Lock icon
    lock_icon = tk.Label(
        root,
        text="🔒",
        font=("Arial", 42),
        bg="#1e1e2f",
        fg="white"
    )
    lock_icon.pack(pady=(30, 5))

    # Title
    title = tk.Label(
        root,
        text="SECURE FILE\nSHARING SYSTEM",
        font=("Arial", 20, "bold"),
        bg="#1e1e2f",
        fg="white"
    )
    title.pack(pady=10)

    # Subtitle
    subtitle = tk.Label(
        root,
        text="Login to continue",
        font=("Arial", 10),
        bg="#1e1e2f",
        fg="lightgray"
    )
    subtitle.pack(pady=5)

    # Username
    username_label = tk.Label(
        root,
        text="Username",
        font=("Arial", 11),
        bg="#1e1e2f",
        fg="white"
    )
    username_label.pack(pady=(30, 5))

    username_entry = tk.Entry(
        root,
        width=28,
        font=("Arial", 12)
    )
    username_entry.pack(ipady=7)

    # Password
    password_label = tk.Label(
        root,
        text="Password",
        font=("Arial", 11),
        bg="#1e1e2f",
        fg="white"
    )
    password_label.pack(pady=(20, 5))

    password_entry = tk.Entry(
        root,
        show="*",
        width=28,
        font=("Arial", 12)
    )
    password_entry.pack(ipady=7)

    # Keyboard navigation

# Press Enter in username field → move to password field
    username_entry.bind(
    "<Return>",
    lambda event: password_entry.focus()
)

# Press Enter in password field → perform login
    password_entry.bind(
    "<Return>",
    lambda event: login()
)

    # Login button
    login_button = tk.Button(
        root,
        text="LOGIN",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=login
    )
    login_button.pack(pady=(35, 15))

    # Register button
    register_button = tk.Button(
        root,
        text="REGISTER",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=register
    )
    register_button.pack(pady=(0, 50))

    # Footer
    footer = tk.Label(
        root,
        text="Python • Tkinter • SQLite • Fernet Encryption",
        font=("Arial", 9),
        bg="#1e1e2f",
        fg="gray"
    )
    footer.pack(side="bottom", pady=20)

# Place cursor automatically in username field
    username_entry.focus()

    root.mainloop()