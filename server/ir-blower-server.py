#!/usr/bin/python

# EG client
# curl -X put -d data=vol_up  http://127.0.0.1:8080/irblower/vol_ctl

import serial, yaml, syslog, sys, os
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask("ir-blower-server")
api = Api(app)

syslog.openlog(logoption=syslog.LOG_PID)

class dict_unpack:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def read_config():
    try:
        with open('../conf/config.yaml', 'r') as config_file:
             settings = yaml.safe_load(config_file)
    except IOError:
        syslog.syslog(syslog.LOG_CRIT, "Failed to read ir-blower config")
        sys.exit(os.EX_IOERR) 

    config_settings = dict_unpack(**settings)
    return(config_settings)


class server_info(Resource):
    def get(self):
      return {"ir-blower-server version" : config_settings.version}


class device_volume(Resource):
    def put(self):
         serial = open_serial()
         serial.open()
         command = request.form['data']

         def change_vol(command):
             if command == "vol_down":
                 print("vol_down")
                 serial.write(b'f')
             elif command == "vol_up":
                 print("vol_up")
             elif command == "vol_mute":
                 print("mute event")
             else:
                 syslog.syslog(syslog.LOG_ERR, "invalid data sent to server")

         change_vol(command)
         serial.close()

class device_power(Resource):
    def put(self):
        serial = open_serial()
        serial.open()
        command = request.form['data']

        def change_power(command):
            if command == "pwr_event":
                print("power event")
            else:
                syslog.syslog(syslog.LOG_ERR, "invalid data sent to server")

        change_power(command)
        serial.close()

class device_input(Resource):
    def put(self):
        serial = open_serial()
        serial.open()
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
                syslog.syslog(syslog.LOG_ERR, "invalid data sent to server")

        change_input(command)
        serial.close()

class device_misc(Resource):
    def put(self):
        serial = open_serial()
        serial.open()
        command = request.form['data']

        def misc_commands(command):
            if command == "gain_sel":
                print("gain event")
            else:
                syslog.syslog(syslog.LOG_ERR, "invalid data sent to server")

        misc_commands(command)
        serial.close()

def run_server():
    config = read_config()
    api.add_resource(server_info, '/irblower/')
    api.add_resource(device_volume, '/irblower/vol_ctl')
    api.add_resource(device_power, '/irblower/pwr_ctl')
    api.add_resource(device_input, '/irblower/in_ctl')
    api.add_resource(device_misc, '/irblower/misc')
    syslog.syslog("Starting ir-blower")
    app.run(host=config.server_address, port=config.port, debug=True)

def open_serial():
    config = read_config()
    serial_device = serial.Serial()
    serial_device.baudrate = 9600
    serial_device.port = config.serial_device
    return(serial_device)

def test_serial():
    try:
        serial = open_serial()
        serial.open()
        serial.close()
    except:
        syslog.syslog(syslog.LOG_CRIT, "failed to open serial device")
        sys.exit(os.EX_UNAVAILABLE)


read_config()
test_serial()
run_server()
