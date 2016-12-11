import operatedoor
from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "Nope."

@app.route("/operate")
def operate():
    operatedoor.operate()
    return "Ok"
