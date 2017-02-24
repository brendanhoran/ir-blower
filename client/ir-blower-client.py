#!/usr/bin/python

import gi, requests, yaml
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


builder = Gtk.Builder()
builder.add_from_file("client-nb.glade")


class dict_unpack:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def read_config():
    with open('config.yaml', 'r') as config_file:
        settings = yaml.safe_load(config_file)

    global config_settings
    config_settings = dict_unpack(**settings)


class Handler:
    def power_button_click(self, button):
        rest_request = requests.put(rest_url+"/pwr_ctl",\
                data = {'data':'pwr_event'})

    def input_next_button_click(self, button):
        rest_request = requests.put(rest_url+"/in_ctl",\
                data = {'data':'in_nxt'})

    def input_previous_button_click(self, button):
        rest_request = requests.put(rest_url+"/in_ctl",\
                data = {'data':'in_prev'})

    def mute_button_click(self, button):
        rest_request = requests.put(rest_url+"/vol_ctl",\
                data = {'data':'vol_mute'})

    def volume_up_button_click(self, button):
        rest_request = requests.put(rest_url+"/vol_ctl",\
                data = {'data':'vol_up'})

    def volume_down_click(self, button):
        rest_request = requests.put(rest_url+"/vol_ctl",\
                data = {'data':'vol_down'})

    def gain_selection_click(self, button):
        print("gain event")

    def input_usb_click(self, button):
        rest_request = requests.put(rest_url+"/in_ctl",\
                data = {'data':'in_usb'})

    def input_optical_input_1_click(self, button):
        rest_request = requests.put(rest_url+"/in_ctl",\
                data = {'data':'in_opt1'})

    def input_optical_input_2_click(self, button):
        rest_request = requests.put(rest_url+"/in_ctl",\
                data = {'data':'in_opt2'})

    def input_coaxial_input_1_click(self, button):
        rest_request = requests.put(rest_url+"/in_ctl",\
                data = {'data':'in_coax1'})

    def input_coaxial_input_2_click(self, button):
        rest_request = requests.put(rest_url+"/in_ctl",\
                data = {'data':'in_coax2'})

builder.connect_signals(Handler())

window = builder.get_object("ir_blower_ui")
window.connect("delete-event", Gtk.main_quit)
window.show_all()


read_config()
rest_url = "http://{0}:{1}/irblower".format\
        (config_settings.server_address,config_settings.port)

Gtk.main()
