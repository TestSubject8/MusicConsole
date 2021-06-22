from gpiozero import Button, LED
import RPi.GPIO as GPIO
import Encoder
from signal import pause
from time import sleep
import functional_console as console
import screen_trial as screen

led_indicate = LED(14)

GPIO.setmode(GPIO.BCM)

def indicate(func):
    def decor(self):
        led_indicate.on()
        sleep(1)
        led_indicate.off()
        func(self)
        return
    return decor

class Menu:
    menu_items = ['Show devices','Switch device','Pause']
    menu_funcs = [console.show_devices, console.switch_device]
    but_next  = Button(26)
    #but_select = Button(3)
    #but_select = Button(3)
    index = 0

    def __init__(self):
        self.but_next.when_pressed = self.next_item
        screen.update_display()
        self.enc = Encoder.Encoder(7,8, self.next_rot)
        pause()

    def next_rot(self):
        val = self.enc.getValue()
        screen.disp_list = [(10,10), str(val)]
        screen.update_display()


    def next_item(self):
        self.index = ( self.index + 1 ) % len(self.menu_items)
        text = self.menu_items[self.index]
        print(text)
        screen.disp_list = [(10,10), str(text)]
        screen.update_display()

    def run_func(self):
        self.menu_funcs[self.index]()


a = Menu()
