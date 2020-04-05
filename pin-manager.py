
# Packages
from flask import Flask, request

# Helpers
from helpers.mongo import PINMongoClient
from helpers.crypto import encrypt_pin, decrypt_pin, encrypt_password
from helpers.validate import (
  validate_assign_pin,
  validate_retreive_pin,
  validate_reset_password,
  is_valid_pin,
  is_valid_card_id,
  is_valid_password,
)

# Flash config
app = Flask(__name__)

# Mongo setup
mongo_client = PINMongoClient()

@app.route("/assign_pin", methods=["POST"])
def assign_pin():
  card_id = request.json["card_id"]
  pin = request.json["pin"]
  password = request.json["password"]

  try:
    validate_assign_pin(card_id, pin, password)
  except Exception as err:
    return err.args[0], 400

  # Encrypt credentials
  encrypted_pin = encrypt_pin(pin)
  encrypted_password = encrypt_password(password)

  # Make query to assign PIN to the DB
  try:
    mongo_client.assign_pin({
      "card_id": card_id,
      "pin": encrypted_pin,
      "password": encrypted_password
    })
  except Exception as err:
    return err.args[0], 500

  return "Success assigning pin", 200

@app.route("/retrieve_pin", methods=["POST"])
def retrieve_pin():
  card_id = request.json["card_id"]
  password = request.json["password"]

  try:
    validate_retreive_pin(card_id, password)
  except Exception as err:
    return err.args[0], 400

  # Ecrypt plain password
  encrypted_password = encrypt_password(password)

  # Make query to get the pin from the DB with card id as parameter
  try:
    card_pin = mongo_client.retrieve_pin(card_id)
  except Exception as err:
    return err.args[0], 404

  # If encrypted plain password and password from DB
  # are equals then we retreive the decrypted PIN
  if encrypted_password == card_pin["password"]:
    decrypted_pin = decrypt_pin(card_pin["pin"])
    return decrypted_pin, 200

  return "Invalid password", 403

@app.route("/reset_password", methods=["PUT"])
def reset_password():
  card_id = request.json["card_id"]
  password = request.json["password"]
  new_password = request.json["new_password"]

  try:
    validate_reset_password(card_id, password, new_password)
  except Exception as err:
    return err.args[0], 400

  encrypted_password = encrypt_password(password)

  try:
    card_pin = mongo_client.retrieve_pin(card_id)
  except Exception as err:
    return err.args[0], 404

  # If encrypted plain password and password from DB
  # are equals then set the new encrypted plain password
  if encrypted_password == card_pin["password"]:
    encrypted_new_password = encrypt_password(new_password)

    mongo_client.set_new_password(card_id, encrypted_new_password)
    return "Success updating password", 200

  return "Invalid password", 403

# We only need this for local development.
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
