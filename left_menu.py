import sys
import RPi.GPIO as GPIO
from signal import pause
import importlib

sys.path.append('modules/')
import modules.Encoder as Encoder
import modules.functional_console as console
from modules.display import display, canvas
# from modules.switch import Switch
# from modules.plpause import PlPause

GPIO.setmode(GPIO.BCM)
for x in [26, 16]:
    GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Tree:
    index1 = 0
    index2 = 0
    items = ['plpause','switch','contrast']
    objs = {}
    def __init__(self):
        self.menu_enc = Encoder.Encoder(27,22, self.change_ind1)
        self.enc = Encoder.Encoder(5,6, self.change_ind2)
        GPIO.add_event_detect(26, GPIO.RISING, callback=self.run_func, bouncetime=400)
        # GPIO.add_event_detect(16, GPIO.RISING, callback=self.run_func, bouncetime=200)
        
        # for i in range(len(self.items)):
            # self.objs.append(importlib.import_module(self.items[i]).Menu(canvas, display, console))
        for i in self.items:
            print('importing ', i)
            self.objs[i] = importlib.import_module(i).Menu(canvas, display, console)
            print('done')
        # self.obj = self.objs[self.items[self.index1]]
        self.change_menu(0)
        pause()

    def change_ind1(self, chan):
        if self.index1 < chan:
            chg = 1
        elif self.index1 > chan:
            chg = -1
        else:
            chg = 0
        self.index1 = chan
        self.index1 %= len(self.items)
        print("index1 ", str(self.index1), str(chg), str(chan))
        self.change_menu(0)

    def change_ind2(self, chan):
        if self.index2 < chan:
            chg = 1
        elif self.index2 > chan:
            chg = -1
        else:
            chg = 0
        self.index2 = chan
        print("index2 ", str(self.index2), str(chg), str(chan))

        # self.enc.value = 0
        self.change_menu(chg)
        
    def change_menu(self, chan):
        self.obj = self.objs[self.items[self.index1]]
        with canvas(display) as draw:
            self.draw_menu(draw)
            self.obj.change_disp(chan, draw)

    # def change_option(self, chan):
    #     obj = self.objs[self.items[self.index1]]
    #     with canvas(display) as draw:
    #         draw.text((0,0), obj.name, fill='white')
    #         obj.change_disp(chan, draw)

    def run_func(self, chan):
        obj = self.objs[self.items[self.index1]]
        with canvas(display) as draw:
            self.draw_menu(draw)
            # draw.text((0,0), obj.name, fill='white')
            obj.run_func(chan, draw)
    
    def draw_menu(self, draw):
        # print(display.bounding_box)
        draw.rectangle(display.bounding_box, fill='black', outline='white')
        draw.line([15,0,15,47], fill='white', width=1)
        draw.text((17,0), self.obj.name, fill='white')
        for i in range(len(self.items)):
            if self.index1 == i:
                draw.rectangle([12,i*9+3,15,i*9+10], fill='white', outline='white')
            draw.text((3,i*9), self.items[i][0] ,fill='white')

Tree()