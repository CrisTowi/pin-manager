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
  def __init__(self):
    self.mongo_client = MongoClient(
      f"mongodb://{username}:{password}@{address}:{port}/{auth_db}?retryWrites=false"
    )

  def assign_pin(self, pin_info):
    db = self.mongo_client.pin_manager

    card_pin = db.pin.find_one({"card_id": pin_info["card_id"]})

    if card_pin["pin"]:
      raise Exception("Card already has a PIN assigned")  

    return db.pin.insert_one(pin_info)

  def retrieve_pin(self, card_id):
    db = self.mongo_client.pin_manager

    card_pin = db.pin.find_one({"card_id": card_id})

    if not card_pin:
      raise Exception("No card with the id")  

    return card_pin

  def set_new_password(self, card_id, new_password):
    db = self.mongo_client.pin_manager

    card_pin = db.pin.find_one({"card_id": card_id})

    if not card_pin:
      raise Exception("No card with the id")

    return db.pin.update({"card_id": card_id}, {"$set": { "password": new_password }})

