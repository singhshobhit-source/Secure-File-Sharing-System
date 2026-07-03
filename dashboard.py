from database import (
    get_files,
    get_encrypted_files,
    delete_latest_file,
    get_total_files
)

from tkinter import messagebox
from file_manager import select_file
from encryption import decrypt_file
from login_window import open_login

import tkinter as tk
import os


# ================= VIEW FILES =================
def view_files():

    files = get_files()

    if not files:
        messagebox.showinfo(
            "Files",
            "No files found."
        )
        return

    output = ""

    for file in files:
        output += f"📄 {file[0]}\n\n"

    messagebox.showinfo(
        "Uploaded Files",
        output
    )


# ================= DOWNLOAD =================
def download_file():

    files = get_encrypted_files()

    if not files:
        messagebox.showinfo(
            "Download",
            "No encrypted files found."
        )
        return

    encrypted_file = files[-1][0]

    decrypt_file(encrypted_file)

    messagebox.showinfo(
        "Success",
        "File decrypted successfully!"
    )


# ================= DELETE =================
def delete_file():

    file = delete_latest_file()

    if not file:
        messagebox.showinfo(
            "Delete",
            "No files found."
        )
        return

    filename = os.path.basename(file[0])

    file_info = (
        "FILE INFORMATION\n\n"
        f"📄 File Name : {filename}\n"
        "🔒 Encrypted : Yes\n"
        "📁 Status : Stored\n\n"
        "Do you want to delete this file?"
    )

    confirm = messagebox.askyesno(
        "Delete Confirmation",
        file_info
    )

    if not confirm:
        return

    try:

        os.remove(file[0])

        messagebox.showinfo(
            "Success",
            "File deleted successfully!"
        )

    except:

        messagebox.showerror(
            "Error",
            "Could not delete file."
        )


# ================= LOGOUT =================
def logout(dashboard):

    dashboard.destroy()
    open_login()


# ================= DASHBOARD =================
def open_dashboard():

    dashboard = tk.Tk()

    dashboard.title("Secure File Sharing System")
    dashboard.geometry("900x600")
    dashboard.configure(bg="#1e1e2f")
    dashboard.resizable(False, False)

    # ================= SIDEBAR =================
    sidebar = tk.Frame(
        dashboard,
        bg="#25253a",
        width=220
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    # Sidebar title
    sidebar_title = tk.Label(
        sidebar,
        text="🔒\nSecure File\nSharing",
        font=("Arial", 18, "bold"),
        bg="#25253a",
        fg="white"
    )

    sidebar_title.pack(pady=30)

    # Upload button
    upload_btn = tk.Button(
        sidebar,
        text="📤 Upload File",
        width=18,
        height=2,
        font=("Arial", 10),
        command=select_file
    )
    upload_btn.pack(pady=10)

    # View button
    view_btn = tk.Button(
        sidebar,
        text="📁 View Files",
        width=18,
        height=2,
        font=("Arial", 10),
        command=view_files
    )
    view_btn.pack(pady=10)

    # Download button
    download_btn = tk.Button(
        sidebar,
        text="📥 Download File",
        width=18,
        height=2,
        font=("Arial", 10),
        command=download_file
    )
    download_btn.pack(pady=10)

    # Delete button
    delete_btn = tk.Button(
        sidebar,
        text="🗑 Delete File",
        width=18,
        height=2,
        font=("Arial", 10),
        command=delete_file
    )
    delete_btn.pack(pady=10)

    # Logout button
    logout_btn = tk.Button(
        sidebar,
        text="🚪 Logout",
        width=18,
        height=2,
        font=("Arial", 10),
        command=lambda: logout(dashboard)
    )
    logout_btn.pack(pady=30)

    # ================= MAIN AREA =================
    main_frame = tk.Frame(
        dashboard,
        bg="#1e1e2f"
    )

    main_frame.pack(
        side="right",
        expand=True,
        fill="both"
    )

    # Title
    title = tk.Label(
        main_frame,
        text="Dashboard",
        font=("Arial", 24, "bold"),
        bg="#1e1e2f",
        fg="white"
    )

    title.pack(pady=30)

    # Statistics card
    stats_frame = tk.Frame(
        main_frame,
        bg="#2d2d44",
        padx=40,
        pady=30
    )

    stats_frame.pack(pady=20)

    total_files = get_total_files()

    stats_title = tk.Label(
        stats_frame,
        text="📊 PROJECT STATISTICS",
        font=("Arial", 14, "bold"),
        bg="#2d2d44",
        fg="white"
    )

    stats_title.pack(pady=5)

    total_label = tk.Label(
        stats_frame,
        text=f"Total Files : {total_files}",
        font=("Arial", 12),
        bg="#2d2d44",
        fg="lightgreen"
)

    total_label.pack(pady=5)
    
# Auto refresh statistics

    def update_stats():

        total = get_total_files()

        total_label.config(
        text=f"Total Files : {total}"
    )

    dashboard.after(
        1000,
        update_stats
    )

    status_label = tk.Label(
        stats_frame,
        text="Status : Active",
        font=("Arial", 12),
        bg="#2d2d44",
        fg="lightblue"
    )

    status_label.pack(pady=5)

    # Welcome text
    welcome = tk.Label(
        main_frame,
        text="Welcome to the Secure File Sharing System",
        font=("Arial", 16),
        bg="#1e1e2f",
        fg="white"
    )

    welcome.pack(pady=40)

    description = tk.Label(
        main_frame,
        text=(
            "This application allows secure file\n"
            "uploading, encryption, decryption,\n"
            "viewing and management."
        ),
        font=("Arial", 12),
        bg="#1e1e2f",
        fg="lightgray"
    )

    description.pack()

    # Footer
    footer = tk.Label(
        main_frame,
        text="Developed using Python • Tkinter • SQLite • Fernet Encryption",
        font=("Arial", 9),
        bg="#1e1e2f",
        fg="gray"
    )

    footer.pack(
    side="bottom",
    pady=20
)

# Start updating statistics
    update_stats()

    dashboard.mainloop()

if __name__ == "__main__":
    open_dashboard()