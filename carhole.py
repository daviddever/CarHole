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

@app.route("/checkdoor")
def check_door():
    door_status = operatedoor.check_door()
    return door_status

if __name__ == "__main__":
    context = ('carholecert.pem', 'carholekey.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=True)
