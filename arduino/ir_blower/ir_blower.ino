// Author  : Brendan Horan
// License : BSD 3-Clause
// Version : 0.0.1
// NOTES   :
//  *  Install a 10uf capacitor between RESET and GND.
//     This prevents the Arduino Nano from restarting
//     on serial port open.
//  *  Physical pin 3 -> IR sender
//  *  Physical pin 4 -> power control
//
// Requires the IRremote library :
// https://github.com/shirriff/Arduino-IRremote
// NOTE some libraries are licensed under other licenses
​
​
#include <IRremote.h>
IRsend irsend;
​
// Variable to hold incoming serial comms
int ctlmsg = 0;   
​
// Define Power controler pin
int pctl = 4;
​
​
void setup() {
        pinMode(pctl,OUTPUT);
        digitalWrite(pctl,HIGH);
        Serial.begin(9600);     
        Serial.println ("Connected:9600");
        Serial.println ("OK");
}
​
​
void loop() {
  
​
        // wait for data
        if (Serial.available() > 0) {
                // read data 
                ctlmsg = Serial.read();
                Serial.print (ctlmsg);
                
​
               // send IR signal based on value from ir-blower server
               // IR-blower-server will send value (1-6, a-f)
               // Arduino client reads the ASCII value and acts on it
               
                switch (ctlmsg) {
                  case 49:
                    // Value 1 
                    // Master 9 input select +
