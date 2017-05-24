// License : BSD 3-Clause
// Version 0.0.1
// Author : Brendan Horan
//
// NOTES :
//   Install a 10uf capacitor between RESET and GND.
//   This prevents the Arduino Nano from restarting
//   on serial port open.

#include <IRremote.h>
IRsend irsend;

// Variable to hold incoming serial comms
int ctlmsg = 0;   

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        Serial.print ("Connected:9600");
}

void loop() {

        // wait for data
        if (Serial.available() > 0) {
                // read data 
                ctlmsg = Serial.read();

                // send IR signal based on value from ir-blower server
               // 49 =1 , 50=2 etc
                switch (ctlmsg) {
                  case 49:
                    Serial.print("49");
                  //  irsend.send
                    break;
                  case 50:
                    Serial.print("50");
                 //   irsend.send
                    break;
                  case 51:
                    Serial.print("51");
                 //   irsend.send
                    break;
                  case 52:
                    Serial.print("52");
                 //   irsend.send
                    break;
                }
               
        }
}
