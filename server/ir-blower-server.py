#!/usr/bin/python

# EG client
# curl -X put -d data=vol_up  http://127.0.0.1:8080/irblower/vol_ctl

import serial, yaml
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask("ir-blower-server")
api = Api(app)


class dict_unpack:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def read_config():
    with open('../conf/config.yaml', 'r') as config_file:
        settings = yaml.safe_load(config_file)

    global config_settings
    config_settings = dict_unpack(**settings)


class server_info(Resource):
    def get(self):
      return {"ir-blower-server version" : config_settings.version}


class device_volume(Resource):
    def put(self):
         command = request.form['data']

         def change_vol(command):
             if command == "vol_down":
                 print("vol_down")
             elif command == "vol_up":
                 print("vol_up")
             elif command == "vol_mute":
                 print("mute event")
             else:
                 print("shit")
                 return {"brr": "brr"}

         change_vol(command)

class device_power(Resource):
    def put(self):
        command = request.form['data']

        def change_power(command):
            if command == "pwr_event":
                print("power event")
            else:
                print("power shit")

        change_power(command)

class device_input(Resource):
    def put(self):
        command = request.form['data']

        def change_input(command):
            if command == "in_nxt":
                print("input next")
            elif command == "in_prev":
                print("input prev")
            elif command == "in_usb":
                print("input usb")
            elif command == "in_opt1":
                print("input optical 1")
            elif command == "in_opt2":
                print("input optical 2")
            elif command == "in_coax1":
                print("input coax 1")
            elif command == "in_coax2":
                print("input coax 2")
            else:
                print("input shit")

        change_input(command)


read_config()

api.add_resource(server_info, '/irblower/')
api.add_resource(device_volume, '/irblower/vol_ctl')
api.add_resource(device_power, '/irblower/pwr_ctl')
api.add_resource(device_input, '/irblower/in_ctl')

app.run(host=config_settings.server_address, port=config_settings.port, debug=True)
