import operatedoor
import config
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def root():
    return 'Nope.'

@app.route('/operate', methods=['POST'])
def operate():
    if request.form['key'] == config.values['door_key']:
        operatedoor.operate(config.values['opener_pin'])
        return 'Ok'
    else:
        return 'Invalid Key'

@app.route('/checkdoor', methods=['POST'])
def check_door():
    if request.form['key'] == config.values['door_key']:
        door_status = operatedoor.check_door(config.values['magnet_pin'])
        return door_status
    else:
        return 'Invalid Key'

if __name__ == '__main__':
    context = (config.values['ssl_cert'], config.values['ssl_key'])
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True)
