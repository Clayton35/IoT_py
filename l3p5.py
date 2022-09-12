# Import required modules
from gpiozero import RGBLED
from time import sleep
import math
import smbus

# Build LED object
led = RGBLED(red = 20, green = 16, blue = 12)

#Build SMBus object
bus = smbus.SMBus(1)

# Get raw data from SMBus(potentiometer)
def get_raw():
        bus.write_byte(0x4b, 0x84)
        sleep(0.1)
        raw = bus.read_byte(0x4b)
        eval(raw)

# Evaluate raw data
def eval(raw):
        val = ((raw / 255) * 360)
        colour(val)

# Convert from input val to LED colour
def colour(val):
        red = math.sin(math.radians(val))
        if red < 0:
                red *= -1

        green = math.sin(math.radians(val + 120))
        if green < 0:
                green *= -1

        blue = math.sin(math.radians(val + 240))
        if blue < 0:
                blue *= -1

        light(red, green, blue)

# Lights up LED according to colour parameters
def light(red, green, blue):
        led.color = (red, green, blue)

# Keeps program running
while True:
        get_raw()
