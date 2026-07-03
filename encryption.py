from cryptography.fernet import Fernet
from database import save_file


# Generate a secret key
def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    return key


# Load existing key
def load_key():
    return open("secret.key", "rb").read()


# Encrypt file
def encrypt_file(filepath):

    key = load_key()
    cipher = Fernet(key)

    # Read original file
    with open(filepath, "rb") as file:
        file_data = file.read()

    # Encrypt data
    encrypted_data = cipher.encrypt(file_data)

    # Create encrypted filename
    encrypted_filename = filepath + ".encrypted"

    # Save encrypted file
    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

    # Save file information in database
    save_file(filepath, encrypted_filename)

    print("File encrypted successfully!")
    print("Encrypted file:", encrypted_filename)


# Decrypt file
def decrypt_file(filepath):

    key = load_key()
    cipher = Fernet(key)

    # Read encrypted file
    with open(filepath, "rb") as file:
        encrypted_data = file.read()

    # Decrypt data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Create decrypted filename
    decrypted_filename = filepath + ".decrypted"

    # Save decrypted file
    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")
    print("Decrypted file:", decrypted_filename)