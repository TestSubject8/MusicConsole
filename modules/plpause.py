import sys
# import RPi.GPIO as GPIO
# import Encoder
from signal import pause
import time
# import functional_console as console
# from display import display, canvas

# GPIO.setmode(GPIO.BCM)
# for x in [26]:
#     GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Menu():
    # but_next  = Button(26)
    # but_select = Button(3)
    # but_select = Button(3)
    # index = 0
    option = 0

    def __init__(self, canvas, display, console):
        self.console = console
        self.canvas = canvas
        self.display = display
        self.name = 'Playback'
        self.text = None
        self.timers = []
        self.get_pback_data()
        # with canvas(display) as draw:
        #     if self.info:
        #         text = 'Playing'
        #     else:
        #         text = 'Paused'
        #     draw.text((0,0), text, fill='white')
        # self.enc = Encoder.Encoder(5,6, self.change_disp)
        # GPIO.add_event_detect(26, GPIO.RISING, callback=self.run_func, bouncetime=200)
        # pause()
    def get_pback_data(self):
        pback = self.console.get_playback()
        if pback:
            self.info = pback['is_playing']
            self.status = "Playing"
        # print(self.info)
            self.vol = pback['device']['volume_percent']
            self.text = str(pback['item']['name'])+'\n'+str(int(pback['progress_ms']/1000))+'/'+str(int(pback['item']['duration_ms']/1000))
        else:
            self.info = False
            self.vol = 50
            self.text = "No playback"
            self.status = 'Not playing'

    def change_disp(self, chan, draw):
        # print("Index at ", str(chan))
        # index = self.enc.getValue()
        # text = self.dev[self.option]['name']
        self.get_pback_data()
        self.vol += chan*5
        if self.vol > 100:
            self.vol = 100
        elif self.vol < 0:
            self.vol = 0

        # draw.text((17,13), text, fill='white')
        # draw.text((22,25), "Volume "+str(self.vol), fill='white')
        if self.info: self.console.vol_change(self.vol)
        self.interface(draw)
        # print(text)
        # get name and id - done - in dev[options]
        # use name to select id to call action func 
        
    def run_func(self, chan, draw):
        self.info = not self.console.plpause()
        # print("function run ", str(func), " on chan ", str(chan))
        self.get_pback_data()
        # draw.text((17,13), str(text), fill='white')
        # draw.text((22,25), "Volume "+str(self.vol), fill='white')
        self.interface(draw)

    def interface(self, draw):
        draw.multiline_text((17,13), self.text, fill='white', spacing = 2)
        draw.text((22,33), "Volume "+str(self.vol), fill='white')

if __name__ == '__main__':
    a = Menu()
