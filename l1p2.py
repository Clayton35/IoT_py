from gpiozero import Button
from gpiozero import LED
import time

# Declaring variables/objects
sig = 0
yellow = LED(21)
btn = Button(20)

# This keeps program running coninuously, then checks for certain conditions
while True:
        # If the value of btn is 1, and sig is 0, print statment and set signal to 1
        # This prevents print statement from printing for every iteration of while loop
        if btn.value==1 and sig == 0 :
                time1 = time.time()
                print('The button is being pressed...')
                sig = 1
        # If the value of btn is 0 and sig is 1(button just released), prints statement and sets sig to 0
        # This prevents print statement from printing for every iteration of while loop
        # Also prints the length of time the button was pressed for.
        elif btn.value==0 and sig == 1:
                time2 = time.time()
                print(f'The button was pressed for {time2-time1:.2f} seconds')
                print('The button is not being pressed...')
                sig = 0
        else:
                continue
