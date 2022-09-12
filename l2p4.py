from gpiozero import Button
from gpiozero import LED
from time import sleep


# Declare variable objects wtih GPIO ports
out1 = LED(12)
out2 = LED(16)
out3 = LED(20)
out4 = LED(21)
out5 = LED(26)
in1 = Button(6 , pull_up=False)

#Setup Truth Table Header
print("\nInput1\tInput2\tInput3\tInput4\tInput5\tReturn")
print("============================================")
#Iterate through possible combinations
for x in range(32):
        input =  '{0:05b}'.format(x)
        tab = str('\t')
        input.split()

        #Assign output value according to generated iteration string value
        out1.value = int(input[0])
        out2.value = int(input[1])
        out3.value = int(input[2])
        out4.value = int(input[3])
        out5.value = int(input[4])
        sleep(0.5)
        # Read output from BB machine.
        ret = int(in1.value)

        # Print values to Truth Table
        print(f"| {int(out1.value)}{tab}  {int(out2.value)}{tab}  {int(out3.value)}{tab}  {int(out4.value)}{tab}  {int(out5.value)}{tab} {str(ret)} |")
        print("============================================")
