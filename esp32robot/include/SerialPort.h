
#pragma once

#include <Arduino.h>
#include <Constants.h>
#include <iostream>

/* Serial Packet Format:
  Device ID: _ _ (2 hexadecimal digits, 0 to 255)
  Message: _0/F_ _ _ (3 hex digits, signed hex, -2048, 2047) -> ideally only use [-255, 255]
  Terminator: , (configurable in Constants.h)

  Sample: 000FF,01FFF, -> device 0 with value 255 and device 1 with value -255
  Reformatted for Clarity: 00 0FF , 01 FFF,
*/

/* Functions:
    String encodeMessage(deviceID, value) // takes in device ID and value -> string
    void sendMessage(deviceID, value) // sends 
*/


class SerialPort
{
    public:
        SerialPort(int baudrate = SERIAL_BAUDRATE); // Serial.begin(baudrate) from arduino 

        bool messageToRead(void); // checks Serial.available() from arduino
        void decodeNextMessage(uint8_t* deviceID, int* value);

        std::string encodePacket(int deviceID, int value); // Takes in device ID and a value, and converts to a hex string
        void sendMessage(std::string message); // takes in list of packets, sends message over serial
};