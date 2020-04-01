from flask import Flask
app = Flask(__name__)

@app.route('/assign_pin', methods=['POST'])
def assign_pin():
  return "Assign pin", 200

@app.route('/retrieve_pin', methods=['POST'])
def retrieve_pin():
  return "Retrieve pin", 200

@app.route('/reset_password', methods=['PUT'])
def reset_password():
  return "Reset password", 200

# We only need this for local development.
if __name__ == '__main__':
  app.run()
