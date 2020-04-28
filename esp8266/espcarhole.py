#! /usr/bin/env python3

import picoweb

app = picoweb.WebApp(__name__)


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Nope.")


@app.route("/operate")
def operate(req, resp):
    # Check if POST request
    method = req.method
    if method == "POST":
        # Check for key
        if request.form["key"] == config.values["door_key"]:
            operatedoor.operate(config.valuesues["opener_pin"])
            yield from picoweb.start_response(resp)
            yield from resp.awrite("Ok")
        else:
            yield from picoweb.start_response(resp)
            yield from resp.awrite("Invalid Key")


@app.route("/checkdoor")
def operate(req, resp):
    # Check if POST request
    method = req.method
    if method == "POST":
        # Check for key
        if request.form["key"] == config.values["door_key"]:
            operatedoor.operate(config.valuesues["opener_pin"])
            door_status = operate_door.check_door(config.values["magnet_pin"])
            yield from picoweb.start_response(resp)
            yield from resp.awrite(door_status)
        else:
            yield from picoweb.start_response(resp)
            yield from resp.awrite("Invalid Key")


import ulogging as logging

logging.basicConfig(level=logging.INFO)

app.run(debug=True)
