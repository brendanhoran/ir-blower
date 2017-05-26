# ir-blower
Client/Server IR sender

Rewrite of the IR blower App and server in Python.

## Requirements    

### server
* pyserial   
* pyyaml   
* flask-restful   
* yaml     

### client
* gi
* yaml
* requests

## Hardware needed
* Arduino Nano or above     
* IR led's and such       
* If you need power control, some safe way of switching mains    


## Configuration file
Right now both server and client use the same config file.    
Configuration is defined in yaml format.     
The following options are supported :      
* version -- should match the release version    
* server_address: IP or DNS name for where the server runs     
* port -- port that the server listens on    
* serial_device -- name of the serial device     

Note : server_address and port are used in both client and server.   


## Example rest commands    

TODO  


## Desktop app
Uses Glade to configure the UI.   
Glade config is "ir-blower-client.glade"  


## TODO   

* add a .desktop link for the UI
* in client UI make the "about" tab usefull vs static
