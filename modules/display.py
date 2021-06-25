from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544, st7735, uc1701x
#from luma.lcd.aux import backlight
from signal import pause
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)

# GPIO.setup(4, GPIO.OUT)

serial = spi(port=0, device=1) #, gpio_DC=24, gpio_RST=25)

display = pcd8544(serial, rotate=0)
# bbox = display.bounding_box
display.show()
display.clear()
display.contrast(56)

# with canvas(display) as draw:
#     draw.text((0,0), "Testing display and rot", fill='white')
# pause()

def draw(a,b):
    with canvas(display) as draw:
        draw.rectangle(display.bounding_box, fill='black', outline='white')
        draw.line([15,0,15,47], fill='white', width=1)
        draw.multiline_text([a,b], "This is a\nsample text", fill='white', spacing=2)
    # pause()

# display.backlight(False)
# draw(17,3)
