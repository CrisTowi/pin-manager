# Standard library
import os

# Packages
from pymongo import MongoClient

address = os.environ["MONGO_ADDRESS"]
port = os.environ["MONGO_PORT"]
username = os.environ["MONGO_USERNAME"]
password = os.environ["MONGO_PASSWORD"]
auth_db = os.environ["MONGO_AUTH_DB"]

class PINMongoClient:
  # Initialize mongo connection
  def __init__(self):
    self.mongo_client = MongoClient(
      f"mongodb://{username}:{password}@{address}:{port}/{auth_db}?retryWrites=false"
    )

  # Assign a new PIN to a card in the DB
  def assign_pin(self, pin_info):
    db = self.mongo_client.pin_manager

    card_pin = db.pin.find_one({"card_id": pin_info["card_id"]})

    # If card PIN doesn't exists then insert it
    if not card_pin:
      return db.pin.insert_one(pin_info)

    # If card PIN already exists then raise an issue
    raise Exception("This card already has a PIN assigned")

  def retrieve_pin(self, card_id):
    db = self.mongo_client.pin_manager

    card_pin = db.pin.find_one({"card_id": card_id})

    # If there is no card with the ID then raise an issue
    if not card_pin:
      raise Exception("No card with the ID")

    return card_pin

  def set_new_password(self, card_id, new_password):
    db = self.mongo_client.pin_manager

    card_pin = db.pin.find_one({"card_id": card_id})

    # If there is no card with the ID then raise an issue
    if not card_pin:
      raise Exception("No card with the ID")

    return db.pin.update({"card_id": card_id}, {"$set": { "password": new_password }})

