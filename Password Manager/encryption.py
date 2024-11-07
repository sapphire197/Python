from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
import base64

# Constants for encryption
SALT_SIZE = 16
KEY_SIZE = 32
NONCE_SIZE = 12
TAG_SIZE = 16

def generate_key(password, salt):
    """Generates a secure key using scrypt."""
    key = scrypt(password.encode(), salt, KEY_SIZE, N=2**14, r=8, p=1)
    return key

def encrypt(password, plaintext):
    """Encrypts plaintext with AES-GCM."""
    salt = get_random_bytes(SALT_SIZE)
    key = generate_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=get_random_bytes(NONCE_SIZE))
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    
    # Encode components for storage
    return base64.b64encode(salt + cipher.nonce + tag + ciphertext).decode('utf-8')

def decrypt(password, encoded_data):
    """Decrypts encoded data with AES-GCM."""
    decoded_data = base64.b64decode(encoded_data)
    salt = decoded_data[:SALT_SIZE]
    nonce = decoded_data[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
    tag = decoded_data[SALT_SIZE + NONCE_SIZE:SALT_SIZE + NONCE_SIZE + TAG_SIZE]
    ciphertext = decoded_data[SALT_SIZE + NONCE_SIZE + TAG_SIZE:]
    
    key = generate_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

def hash_master_password(password):
    """Hashes the master password for secure storage."""
    salt = get_random_bytes(SALT_SIZE)
    hashed_password = scrypt(password.encode(), salt, KEY_SIZE, N=2**14, r=8, p=1)
    return base64.b64encode(salt + hashed_password).decode('utf-8')

def verify_master_password(stored_hash, password):
    """Verifies the master password."""
    decoded_hash = base64.b64decode(stored_hash)
    salt = decoded_hash[:SALT_SIZE]
    stored_key = decoded_hash[SALT_SIZE:]
    derived_key = scrypt(password.encode(), salt, KEY_SIZE, N=2**14, r=8, p=1)
    return derived_key == stored_key

