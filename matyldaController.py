import sys
import smbus2 as smbus 
import time
# Slave Addresses
I2C_SLAVE_ADDRESS = 11 #0x0b - 11

# This function converts a string to an array of bytes.
def ConvertStringsToBytes(src):
  converted = []
  for b in src:
    converted.append(ord(b))
  return converted

def main(args):
    # Create the I2C bus
    I2Cbus = smbus.SMBus(1)
    with smbus.SMBus(1) as I2Cbus:
        slaveAddress = I2C_SLAVE_ADDRESS

        BytesToSend = ConvertStringsToBytes("3,45,90")
        print("Sent " + str(slaveAddress) + " the " + str("3,45,90") + " command.")
        print(BytesToSend )

        I2Cbus.write_i2c_block_data(slaveAddress, 0x00, BytesToSend)
        
        time.sleep(0.5)
        while True:
            try:
                data=I2Cbus.read_i2c_block_data(slaveAddress,0x00,16)
                print("recieve from slave:")
                print(data)
            except:
                print("remote i/o error")
                time.sleep(0.5)
    return 0


if __name__ == '__main__':
     try:
        main(sys.argv)
     except KeyboardInterrupt:
        print("program was stopped manually")
     input()