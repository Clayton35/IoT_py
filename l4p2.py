# Import necessary Libraries
from gpiozero import Button

#Build button objects
A = Button(21)
B = Button(20)
btn = Button(16)

# Define function for evaluating clockwise/counter-clockwise rotation
def clockwise():
        if B.value == 0:
                print("Clockwise rotation")
        elif B.value == 1:
                print("Counter-Clockwise Rotation")

# Define function for button press event
def press():
        print("Button was pressed")

#Callback event functions for rotation/button press
A.when_pressed = clockwise
btn.when_pressed = press

# Keeps program running
while True:
        pass
