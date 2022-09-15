# Import necessary modules
import I2C_LCD_Driver as lcd_d

# Build LCD object
lcd = lcd_d.lcd()

# Build character bitmaps
symbol = [[0b01010, 0b01010, 0b01010, 0b00000, 0b10001, 0b10001, 0b10001, 0b01110], [0b00000, 0b11111, 0b01110, 0b00100, 0b01110, 0b11111, 0b00000]]

# Load bitmap
lcd.lcd_load_custom_chars(symbol)

# Write custom char to LCD
lcd.lcd_clear()
lcd.lcd_write_char(0)
lcd.lcd_write_char(1)
