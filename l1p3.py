from gpiozero import Button
from gpiozero import LED
import time, signal

# Declaring variables/objects
red = LED(21)
yellow = LED(26)
green = LED(19)
btn = Button(20)
slide = Button(12)

# Defines the function for the event of pressing button
def press_func():
        # Makes time_start a global variable so release_func can also manipulate it
        global time_start
        # Stores the time-since-epoch in time_start when the button is pressed
        time_start = time.time()
        # Checks to see if slide button is engaged, and responds accordingly
        if slide.value==0:
                red.on()
                print('Button is being pressed, but slider is off.')
        elif slide.value==1:
                yellow.on()
                print('Button is on, slider is on.')

# Defines the function for the event of releasing the button
def release_func():
        # Stores the time-since-epoch in time_end whent he button is released
        time_end = time.time()
        # This stores the value in seconds of the time the botton was pressed for
        time_total = time_end - time_start
        # Checks to see if slide is engaged and button is pressed for at least 7 seconds, then activates all LEDs
        if slide.value==1 and time_total > 7:
                red.on()
                yellow.on()
                green.on()
                print('Slide is on, button was pressed for %2d seconds.' % time_total)
        # If the slide is off when button is pressed, this turns off any lit LEDs and continues interating while-loop
        else:
                red.off()
                yellow.off()
# These are the callback functions that are triggered by specified events (press/release)
btn.when_pressed = press_func
btn.when_released = release_func

# Keeps program running until conditions are met
while True:
        pass
