# Standard library
import os

# Packages
from cryptography.fernet import Fernet

# Set Fermet encryption
fernet_token = os.environ["FERNET_TOKEN"]
key = fernet_token.encode("utf-8")
f = Fernet(key)

# Encrypt PIN with Fernet encryption scheme
def encrypt_pin(pin):
  return f.encrypt(pin.encode("utf-8"))

# Decrypt PIN with Fernet encryption scheme
def decrypt_pin(pin):
  return f.decrypt(pin)

# Encrypt password with hashing algoritm
def encrypt_password(password):
  return hash(password)
