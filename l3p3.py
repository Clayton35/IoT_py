# Importing required modules
from gpiozero import PWMLED, LED
from time import sleep

# Creating object called green of PWMLED type on GPIO 16
green = PWMLED(16)

# Assigning frequency of 200Hz
green.frequency=200

#Assigning duty cycles of 25% and 75% respectively
green.value=0.25
print("Frequency = %d Hz Duty Cycle = %d" % (green.frequency, (green.value * 100)))
sleep(60)
green.value=0.75
print("Frequency = %d Hz Duty Cycle = %d" % (green.frequency, (green.value * 100)))
sleep(60)

# Assigning frequency of 1kHz
green.frequency=1000

#Assigning duty cycles of 10% and 90% respectively
green.value=0.1
print("Frequency = %d Hz Duty Cycle = %d" % (green.frequency, (green.value * 100)))
sleep(60)
green.value=0.9
print("Frequency = %d Hz Duty Cycle = %d" % (green.frequency, (green.value * 100)))
sleep(60)


# Fades light on over 1sec
for x in range(100):
        green.value=float(x/100)
        sleep(0.01)
# Fades light out over 1sec
for x in range(100, 0, -1):
        green.value=float(x/100)
        sleep(0.01)
