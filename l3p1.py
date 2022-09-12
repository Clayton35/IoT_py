# This imports modules to be used in this program
from gpiozero import LEDBoard
from time import sleep

# This creates an LEDBoard oject called board that connects to 7-seg display via specified GPIO

board = LEDBoard(12, 16, 20, 21, 5, 6, 13, 19)

# This is a list of lists that maps out each LED in the display separately - counts 0-9
bitmap = [[0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 0, ], [1, 0, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0]]

# This iterates through the bitmap list and assigns values to board.value to light up specific LED
for dig in bitmap:
        board.value  = dig
        sleep(0.5)
        board.off()
