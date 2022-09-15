# Import necessary modules
import I2C_LCD_Driver as lcd_d

# Build LCD object
lcd = lcd_d.lcd()

# Print Message to LCD Screen
lcd.lcd_display_string("     Clayton ")
lcd.lcd_display_string("    Davidson  ", 2)
