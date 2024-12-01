from cryptography.fernet import Fernet
import os

# Generate or load encryption key
def load_or_create_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

# Encrypt the note
def encrypt_note():
    note = input("Enter the note to encrypt: ").encode()
    fernet = Fernet(load_or_create_key())
    encrypted = fernet.encrypt(note)
    with open("notes.enc", "ab") as enc_file:
        enc_file.write(encrypted + b"\n")
    print("Note encrypted and saved.")

# Decrypt and display all notes
def decrypt_notes():
    if not os.path.exists("notes.enc"):
        print("No encrypted notes found.")
        return
    fernet = Fernet(load_or_create_key())
    with open("notes.enc", "rb") as enc_file:
        lines = enc_file.readlines()
    print("\nDecrypted Notes:")
    for line in lines:
        print(fernet.decrypt(line.strip()).decode())

if __name__ == "__main__":
    while True:
        print("\nEncrypted Notes App")
        print("1. Add a new encrypted note")
        print("2. View all decrypted notes")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            encrypt_note()
        elif choice == "2":
            decrypt_notes()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
