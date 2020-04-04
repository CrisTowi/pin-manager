import os
from pymongo import MongoClient

address = os.environ["MONGO_ADDRESS"]
port = os.environ["MONGO_PORT"]
username = os.environ["MONGO_USERNAME"]
password = os.environ["MONGO_PASSWORD"]

class PINMongoClient:
  def __init__(self):
    self.mongo_client = MongoClient(
      f'mongodb://{username}:{password}@{address}:{port}/pin_manager?retryWrites=false'
    )

  def assign_pin(self, pin_info):
    db = self.mongo_client.pin_manager

    return db.pin.insert_one(pin_info)

  def retrieve_pin(self, client_id):
    db = self.mongo_client.pin_manager

    return db.pin.find_one({'client_id': client_id})

  def set_new_password(self, client_id, new_password):
    db = self.mongo_client.pin_manager

    return db.pin.update({'client_id': client_id}, {'$set': { 'password': new_password }})

