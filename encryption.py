from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
import base64
import os

# Define constants
SALT = b"your_salt_value"  # Replace with a secure, unique salt for each installation
KEY_LENGTH = 32  # AES-256 requires a 32-byte key
NONCE_SIZE = 12  # AES-GCM recommended nonce size
HASH_ITERATIONS = 16384

def derive_key(password: str) -> bytes:
    """Derives a secure key using scrypt from the given password."""
    return scrypt(password.encode(), SALT, KEY_LENGTH, N=HASH_ITERATIONS, r=8, p=1)

def encrypt(data: str, key: bytes) -> str:
    """Encrypts data with AES-GCM and returns the encrypted string in base64 format."""
    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(nonce + tag + ciphertext).decode()

def decrypt(encrypted_data: str, key: bytes) -> str:
    """Decrypts AES-GCM encrypted data from base64 format."""
    data = base64.b64decode(encrypted_data)
    nonce = data[:NONCE_SIZE]
    tag = data[NONCE_SIZE:NONCE_SIZE + 16]
    ciphertext = data[NONCE_SIZE + 16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

def hash_master_password(master_password: str) -> str:
    """Hashes the master password for secure storage."""
    return base64.b64encode(derive_key(master_password)).decode()

def verify_master_password(input_password: str, stored_password: str) -> bool:
    """Verifies if the provided master password matches the stored hashed password."""
    return hash_master_password(input_password) == stored_password
