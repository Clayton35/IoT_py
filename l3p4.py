# Import required modules
import smbus
from gpiozero import PWMLED
from time import sleep

# Create object called green of PWMLED type on GPIO16
green = PWMLED(16)

# Create an object called bus of SMBus type
bus = smbus.SMBus(1)

# Setting frequency to 1kHz
green.frequency=1000

# Defines function to write data(0x84) to bus
def writeData():
        bus.write_byte(0x4b, 0x84)
        sleep(0.1)

# Defines function to read data from bus
def readData():
        data = bus.read_byte(0x4b)
        return data

# Evaluates the raw data(int from 0-255) into a value from 0 to 1
def eval(raw):
        val = float((1 / 256) * int(raw))
        return val

# Passes the value to the PWMLED object
def light(val):
        green.value=val

# Iterates continuously
while True:
        writeData()
        raw = readData()
        val = eval(raw)
        light(val)
