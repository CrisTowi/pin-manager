import re

# Check if pin is valid with 4 digits
def is_valid_pin(pin):
  return type(pin) == str and bool(re.match(r"^(\d{4})$", pin))

# Check if pin is valid with 16 digits
def is_valid_card_id(card_id):
  return type(card_id) == str and bool(re.match(r"^(\d{16})$", card_id))

# Check if pin is valid with at least 3 and less than 30 characters
def is_valid_password(password):
  return type(password) == str and len(password) > 3 and len(password) < 30

def validate_assign_pin(card_id, pin, password):
  if not is_valid_card_id(card_id):
    raise Exception("Invalid card ID")
  elif not is_valid_pin(pin):
    raise Exception("Invalid PIN")
  elif not is_valid_password(password):
    raise Exception("Invalid password")

def validate_retreive_pin(card_id, password):
  if not is_valid_card_id(card_id):
    raise Exception("Invalid card ID")
  elif not is_valid_password(password):
    raise Exception("Invalid password")

def validate_reset_password(card_id, password, new_password):
  if not is_valid_card_id(card_id):
    raise Exception("Invalid card ID")
  elif not is_valid_password(password):
    raise Exception("Invalid password")
  elif not is_valid_password(new_password):
    raise Exception("Invalid new password")
