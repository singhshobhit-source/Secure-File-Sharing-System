from tkinter import filedialog
from encryption import encrypt_file


def select_file():

    filepath = filedialog.askopenfilename()

    if filepath:
        print("Selected file:")
        print(filepath)

        encrypt_file(filepath)

    return filepath