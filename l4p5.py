# Import necessary modules/tools
import I2C_LCD_Driver as lcd_d
from gpiozero import Button
import dht11_library as dht11
import RPi.GPIO as gpio
from time import sleep
import smbus

# Build LCD object
display = lcd_d.lcd()


# Initialize GPIO for Temp/Humidity sensor
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.cleanup()
instance = dht11.DHT11(12)

# Flag objects/ global variables
dirFlag = 0
menuVal = 0
selectFlag = 0
voltFlag = 0
result = 0
voltage = 0.0

# Print Menu Greeting
display.lcd_display_string("      Menu ")
display.lcd_display_string("Scroll for optns", 2)

# Build rotary encoder/button objects for menu control
A = Button(21)
B = Button(20)
btn = Button(16)

# Define function to determine rotation direction
def direction():
        global dirFlag
        global selectFlag
        global menuVal
        if B.value == 0:
                if menuVal < 3:
                        menuVal+=1
                else:
                        menuVal = 0
        else:
                if menuVal > 0:
                        menuVal-=1
                else:
                        menuVal = 3

        if selectFlag == 1:
                pass

        menu_vals()

# Define Menu Values
def menu_vals():
        global menuVal
        display.lcd_clear()
        if menuVal == 0:
                display.lcd_display_string("Temperature")
        elif menuVal == 1:
                display.lcd_display_string("Humidity")
        elif menuVal == 2:
                display.lcd_display_string("Voltage")
        elif menuVal == 3:
                display.lcd_display_string("Exit")
        else:
                print("Error!")

#Define selection function
def select():
        global selectFlag
        if selectFlag == 0:
                selectFlag = 1
                option_val()
        elif selectFlag == 1:
                selectFlag = 0
                menu_vals()

# Define function to display chosen option
def option_val():
        global menuVal
        global selectFlag
        global Rfid
        global result
        global voltFlag
        global voltage
        global instance

        if selectFlag == 1:
                display.lcd_clear()
                result = instance.read()
                if menuVal == 0:
                        display.lcd_display_string("%.02f c" % result.temperature, 2)
                elif menuVal == 1:
                        display.lcd_display_string("%.02f %%" % result.humidity, 2)
                elif menuVal == 2:
                        if voltFlag == 0:
                                voltFlag = 1
                                volt_write()
                        else:
                                display.lcd_display_string("%.02f V" % voltage, 2)
                                voltFlag = 0
                elif menuVal == 3:
                        display.lcd_display_string("    Goodbye!")
                        sleep(2)
                        display.lcd_clear()
                        exit(-1)
                sleep(0.5)

# Define voltage sensor functions
def volt_write():
        bus = smbus.SMBus(1)
        bus.write_byte(0x4b, 0x84)
        bus.close()
        sleep(0.1)
        volt_read()

def volt_read():
        global voltage
        bus = smbus.SMBus(1)
        data = bus.read_byte(0x4b)
        voltage = ((3.3 / 256) * int (data))
        option_val()

# Callback event functions
A.when_pressed = direction
btn.when_pressed = select

# Keeps program running
while True:
        if selectFlag == 1:
                option_val()
        pass
