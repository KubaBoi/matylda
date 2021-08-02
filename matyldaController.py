# -*- coding: utf-8 -*-
import smbus2
import time
# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus2.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeData(value):
    byteValue = StringToBytes(value)    
    bus.write_i2c_block_data(address,0x00,byteValue) #first byte is 0=command byte.. just is.

    print("Sending: " + value)


def StringToBytes(val):
        retVal = []
        for c in val:
            retVal.append(ord(c))
        return retVal

while True:
    try:
        writeData("1,45,90")  
        time.sleep(5)
        writeData("1,45,0")
        time.sleep(5)
    except Exception as e:
        print("Arduino " + str(address) + " disconnected")