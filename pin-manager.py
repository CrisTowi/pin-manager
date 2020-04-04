# Packages
from flask import Flask, request
from cryptography.fernet import Fernet

# Helpers
from helpers.mongo import PINMongoClient

# Flash config
app = Flask(__name__)

# Mongo setup
mongo_client = PINMongoClient()

key = Fernet.generate_key()
f = Fernet(key)

@app.route("/assign_pin", methods=["POST"])
def assign_pin():
  client_id = request.json["client_id"]
  pin = request.json["pin"]
  password = request.json["password"]

  encripted_pin = f.encrypt(pin.encode("utf-8"))
  encripted_password = hash(password)

  mongo_client.assign_pin({
    "client_id": client_id,
    "pin": encripted_pin,
    "password": encripted_password
  })

  return "Success", 200

@app.route("/retrieve_pin", methods=["POST"])
def retrieve_pin():
  client_id = request.json["client_id"]
  password = request.json["password"]

  client_pin = mongo_client.retrieve_pin(client_id)

  if hash(password) == client_pin["password"]:
    decrpyt_pin = f.decrypt(client_pin["pin"])
    return decrpyt_pin, 200

  return "Invalid password", 403

@app.route("/reset_password", methods=["PUT"])
def reset_password():
  client_id = request.json["client_id"]
  password = request.json["password"]
  new_password = request.json["new_password"]

  client_pin = mongo_client.retrieve_pin(client_id)

  if hash(password) == client_pin["password"]:
    mongo_client.set_new_password(client_id, hash(new_password))
    return "Success", 200

  return "Invalid password", 403

# We only need this for local development.
if __name__ == "__main__":
  app.run()
