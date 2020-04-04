# Standard library
import os

# Packages
from cryptography.fernet import Fernet

fernet_token = os.environ["FERNET_TOKEN"]

key = fernet_token.encode("utf-8")
f = Fernet(key)

def encrypt_pin(pin):
  return f.encrypt(pin.encode("utf-8"))

def decrypt_pin(pin):
  return f.decrypt(pin)

def encrypt_password(password):
  return hash(password)
