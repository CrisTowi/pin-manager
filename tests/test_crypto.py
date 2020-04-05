# Packages
import pytest

# Helpers
from helpers.crypto import encrypt_pin, decrypt_pin, encrypt_password

def test_encrypt_pin():
  plain_pin = "1234"

  assert plain_pin != encrypt_pin(plain_pin)

def test_decrypt_pin():
  plain_pin = "1234"

  encrypted_pin = encrypt_pin(plain_pin)
  plain_pin = decrypt_pin(encrypted_pin)

  assert plain_pin == plain_pin

def test_encrypt_password():
  plain_password = "my_new_password"

  assert plain_password != encrypt_password(plain_password)
