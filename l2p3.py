from gpiozero import Button
from gpiozero import LED
import subprocess

# Declaring variables/objects with GPIO
btn1 = Button(12)
btn2 = Button(16)
btn3 = Button(20)
btn4 = Button(21)
btn5 = Button(5)
led = LED(26)

# Defines what to do when button is pressed
def event():
        # Starts a thread running my ./p1 (blackbox) program, with button values as the arguments
        ret = subprocess.call(["./p1", str(btn1.value), str(btn2.value), str(btn3.value), str(btn4.value), str(btn5.value)])
        # If the return value of thread is 1(passes logic in blackbox) turn led on
        if (int(ret) != 0):
                led.on()
        #Otherwise, turn off led
        else:
                led.off()

# Callback functions for reactions to button input
btn1.when_pressed = event
btn1.when_released = event
btn2.when_pressed = event
btn2.when_released = event
btn3.when_pressed = event
btn3.when_released = event
btn4.when_pressed = event
btn4.when_released = event
btn5.when_pressed = event
btn5.when_released = event

# Keeps program running until cancelled.
while True:
        pass
