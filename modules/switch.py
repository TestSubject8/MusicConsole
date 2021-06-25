# import sys
# import RPi.GPIO as GPIO
# import Encoder
from signal import pause
# import time
# import functional_console as console
# from display import display, canvas

# GPIO.setmode(GPIO.BCM)
# for x in [26]:
#     GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Menu():
    # but_next  = Button(26)
    # but_select = Button(3)
    # but_select = Button(3)
    option = 0

    def __init__(self, canvas, display, console):
        # self.but_next.when_pressed = self.next_item
        self.console = console
        self.name = "Devices"
        self.dev = console.show_devices()['devices']
        self.current = console.get_playback()['device']['name']
        #TODO - run this to refresh list of devices - after the console fix for caching login tokens
        self.canvas = canvas
        self.display = display
        # self.menu_items = [('Switch device', console.show_devices)]
        # self.menu_funcs = [console.switch_device]
        # with canvas(display) as draw:
        #     text = self.dev[self.option]['name']
        #     draw.text((0,10), text, fill='white')
        # self.enc = Encoder.Encoder(5,6, self.change_disp)
        # GPIO.add_event_detect(26, GPIO.RISING, callback=self.run_func, bouncetime=200)
        # pause()

    def change_disp(self, chan, draw):
        # print("Index at ", str(chan))
        # index = self.enc.getValue()
        self.option += chan 
        self.option %= len(self.dev)
        self.interface(draw)
        # get name and id - done - in dev[options]
        # use name to select id to call action func
        
    def run_func(self, chan, draw):
        info = self.console.switch_device(self.dev[self.option]['id'])
        # print("function run ", str(func), " on chan ", str(chan))
        self.dev = self.console.show_devices()['devices']
        # if not info:
        #     info = "Switched device \nto "+str(self.dev[self.option]['name'])
        self.current = self.dev[self.option]['name']
        self.interface(draw)
        # draw.multiline_text((22,25), str(info), fill='white')

    # TODO - timed callback to refresh the device list (self.dev)

    def interface(self, draw):
        for i in range(len(self.dev)):
            text = self.dev[i]['name']
            if self.option == i:
                draw.rectangle([17,i*9+10,20,i*9+17], fill='black', outline='white')
            if text == self.current:
                draw.rectangle([19,i*9+10,20,i*9+17], fill='white', outline='white')
            draw.text((22,i*9+8), text, fill='white')

if __name__ == '__main__':
    a = Menu()
