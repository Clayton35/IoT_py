#  Import necessary modules
import smbus
from time import sleep

# Function to write command data
def writeData():
        bus = smbus.SMBus(1)
        bus.write_byte(0x4b, 0x84)
        bus.close()
        sleep(0.1)
        readData()

# Function to read returning data from A-D Converter
def readData():
        bus = smbus.SMBus(1)
        data = bus.read_byte(0x4b)
        print("Data value is % d" % int(data)) # This prints data value 0-255
        print("Voltage is %0.2f V" % ((3.3 / 256) * int(data))) # This prints voltage 0 - 3.3V
        bus.close()


# This keeps the program running
while True:
        writeData()
