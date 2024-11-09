from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_content(content):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(content.encode())

def decrypt_content(encrypted_content):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_content).decode()

if __name__ == "__main__":
    generate_key()
    print("Encryption key generated.")
