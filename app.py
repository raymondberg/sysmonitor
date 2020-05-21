import subprocess

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return subprocess.check_output(["df", "-h"])

@app.route('/ping')
def ping():
    return subprocess.check_output(["ping", "-c", "1", "google.com"])
