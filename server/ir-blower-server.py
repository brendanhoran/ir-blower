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
                 serial.write(b"5")
                 serial.close()
             elif command == "vol_up":
                 print("vol_up")
                 serial.close()
                 serial.write(b"4")
             elif command == "vol_mute":
                 print("mute event")
                 serial.write(b"3")
                 serial.close()
             else:
                 syslog.syslog(syslog.LOG_ERR, "Invalid data sent to server")

         change_vol(command)

class device_power(Resource):
    def put(self):
        serial = open_serial()
        serial.open()
        command = request.form['data']

        def change_power(command):
            if command == "pwr_event":
                print("power event")
                serial.write(b"6")
                serial.close()
            else:
                syslog.syslog(syslog.LOG_ERR, "Invalid data sent to server")

        change_power(command)

class device_input(Resource):
    def put(self):
        serial = open_serial()
        serial.open()
        command = request.form['data']

        def change_input(command):
            if command == "in_nxt":
                print("input next")
                serial.write(b"1")
                serial.close()
            elif command == "in_prev":
                print("input prev")
                serial.write(b"2")
                serial.close()
            elif command == "in_usb":
                print("input usb")
                serial.write(b"a")
                serial.close()
            elif command == "in_opt1":
                print("input optical 1")
                serial.write(b"d")
                serial.close()
            elif command == "in_opt2":
                print("input optical 2")
                serial.write(b"e")
                serial.close()
            elif command == "in_coax1":
                print("input coax 1")
                serial.write(b"b")
                serial.close()
            elif command == "in_coax2":
                print("input coax 2")
                serial.write(b"c")
                serial.close()
            else:
                syslog.syslog(syslog.LOG_ERR, "Invalid data sent to server")

        change_input(command)

class device_misc(Resource):
    def put(self):
        serial = open_serial()
        serial.open()
        command = request.form['data']

        def misc_commands(command):
            if command == "gain_sel":
                print("gain event")
                serial.write(b"f")
                serial.close()
            else:
                syslog.syslog(syslog.LOG_ERR, "Invalid data sent to server")

        misc_commands(command)

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
        syslog.syslog(syslog.LOG_CRIT, "Failed to open serial device")
        sys.exit(os.EX_UNAVAILABLE)


read_config()
test_serial()
run_server()
