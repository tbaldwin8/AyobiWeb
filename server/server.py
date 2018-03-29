import hashlib
from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/api/input', methods=['POST'])
def sample():
  name = request.form['name']
  return "name"


@app.route('/login', methods=['POST'])
def login():
  # get salt, name, and use hashlib to authenticate
  resp = make_response('')
  resp.set_cookie('ayobi_auth', "SAMPLE")
  return resp
