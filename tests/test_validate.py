# Packages
import pytest

# Helpers
from helpers.validate import is_valid_pin, is_valid_card_id, is_valid_password

def test_is_valid_pin():
  pin = "1234"
  assert is_valid_pin(pin) == True
  pin = "12345"
  assert is_valid_pin(pin) == False
  pin = 12345
  assert is_valid_pin(pin) == False

def test_is_valid_card_id():
  card_id = "1234567890123456"
  assert is_valid_card_id(card_id) == True
  card_id = "12345678901234567"
  assert is_valid_card_id(card_id) == False
  card_id = 1234567890123456
  assert is_valid_card_id(card_id) == False

def test_is_valid_password():
  password = "my_new_password"
  assert is_valid_password(password) == True
  password = "pas"
  assert is_valid_password(password) == False
  password = 1234
  assert is_valid_password(password) == False
