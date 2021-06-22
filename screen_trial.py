from gpiozero import Button, LED
import  RPi.GPIO as gpio
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544
from signal import pause

serial = spi(port=0, device=1)

gpio.setup(7, gpio.OUT)
gpio.output(7, gpio.HIGH)

display = pcd8544(serial, rotate=0)

display.show()
display.clear()
display.contrast(50)

disp_list = [((10,10),'Spotipy initialized'), ((10,20), '\tLogged in')]

def standard_display(draw):
    draw.rectangle(display.bounding_box, outline='white', fill='black')

def display_text(draw, disp_list):
    # draw.text((10,10), 'hello', fill='white')
    for obj in disp_list:
        draw.text(obj[0], obj[1], fill='white')

def update_display():
    with canvas(display) as draw:
        standard_display(draw)
        display_text(draw, disp_list)
    pause()

if __name__ == '__main__':
    update_display()