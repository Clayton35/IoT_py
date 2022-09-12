#Clayton Davidson - 000860643  Jan19/22
from gpiozero import LED
from time import sleep
from signal import pause

led = LED(21)

#This turns the LED on/off with 10s pause.
led.on()
sleep(5)
led.off()

#This makes the LED blink at 0.5s interval using loops
count = 0
while count < 10:
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
        count+=1

sleep(5)

#This makes the LED blink at 0.5s interval using blink method
led.blink(0.5, 0.5, 10, True)
pause()
