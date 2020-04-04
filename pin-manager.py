# Standard libraries
import os
import random

# Packages
from Crypto.Cipher import AES
from flask import Flask, request

# Helpers
from helpers.mongo import PINMongoClient

# Flash config
app = Flask(__name__)

# Cripto
key = os.environ['CRIPTO_KEY']
iv = os.environ['CRIPTO_IV']
aes = AES.new(key, AES.MODE_CBC, iv)

# Mongo setup
mongo_client = PINMongoClient()

@app.route('/assign_pin', methods=['POST'])
def assign_pin():
  client_id = request.json['client_id']
  pin = request.json['pin']
  password = request.json['password']

  encripted_pin = aes.encrypt(pin*16)
  encripted_password = hash(password)

  mongo_client.assign_pin({
    'client_id': client_id,
    'pin': encripted_pin,
    'password': encripted_password
  })

  return 'Success', 200

@app.route('/retrieve_pin', methods=['POST'])
def retrieve_pin():
  client_id = request.json['client_id']
  password = request.json['password']

  client_pin = mongo_client.retrieve_pin(client_id)

  decrpyttext = aes.decrypt(client_pin['pin'])
  decrpyttext = decrpyttext[-(len(decrpyttext)//16): len(decrpyttext)]

  if hash(password) == client_pin['password']:
    return decrpyttext, 200

  return 'Invalid password', 403

@app.route('/reset_password', methods=['PUT'])
def reset_password():
  client_id = request.json['client_id']
  password = request.json['password']
  new_password = request.json['new_password']

  client_pin = mongo_client.retrieve_pin(client_id)

  if hash(password) == client_pin['password']:
    mongo_client.set_new_password(client_id, hash(new_password))
    return 'Success', 200

  return 'Invalid password', 403

# We only need this for local development.
if __name__ == '__main__':
  app.run()
