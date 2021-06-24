from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544, st7735, uc1701x
#from luma.lcd.aux import backlight
from signal import pause
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

serial = spi(port=0, device=1) #, gpio_DC=24, gpio_RST=25)

display = pcd8544(serial, rotate=0)

display.show()
display.clear()
display.contrast(50)

with canvas(display) as draw:
    draw.text((0,0), "Testing display and rot", fill='white')
# pause()