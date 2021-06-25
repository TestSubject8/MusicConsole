import sys
import RPi.GPIO as GPIO
# import Encoder
from signal import pause
import time
# import functional_console as console
# from display import display, canvas

GPIO.setmode(GPIO.BCM)
# for x in [26]:
#     GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Menu():
    # but_next  = Button(26)
    # but_select = Button(3)
    # but_select = Button(3)
    # index = 0
    option = 56

    def __init__(self, canvas, display, console):
        self.console = console
        self.canvas = canvas
        self.display = display
        self.name = 'Contrast'
        display.contrast(self.option)
        self.light = False
        
    def change_disp(self, chan, draw):
        # print("Index at ", str(chan))
        # index = self.enc.getValue()
        # text = self.dev[self.option]['name']
        self.option += chan
        if self.option > 80:
            self.option = 80
        elif self.option < 30:
            self.option = 30
        
        self.display.contrast(self.option)
        self.interface(draw)
        # print(text)
        # get name and id - done - in dev[options]
        # use name to select id to call action func 
        
    def run_func(self, chan, draw):
        # self.info = self.console.plpause()
        # print("function run ", str(func), " on chan ", str(chan))
        # if self.info:
            # text = 'Playing'
        # else:
            # text = 'Paused'
        # draw.text((17,13), str(text), fill='white')
        # draw.text((22,25), "Volume "+str(self.vol), fill='white')
        # self.interface(draw)
        if not self.light:
            GPIO.output(4, GPIO.HIGH)
            self.light = True
        else:
            GPIO.output(4, GPIO.LOW)
            self.light = False

    def interface(self, draw):
        # draw.text((17,13), "Contrast", fill='white')
        draw.text((17,13), str(self.option), fill='white')

if __name__ == '__main__':
    a = Menu()
