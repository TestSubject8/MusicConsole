import sys
sys.path.append("../")
import RPi.GPIO as GPIO
import Encoder
from signal import pause
from time import sleep
import functional_console as console
from display import display, canvas

GPIO.setmode(GPIO.BCM)
for x in [26]:
    GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Menu:
    menu_items = [('Show devices',None),('Switch device', None),('Pause', None), ('Volume', console.get_vol)]
    menu_funcs = [console.show_devices, console.switch_device, console.plpause, console.vol_change]
    # but_next  = Button(26)
    # but_select = Button(3)
    # but_select = Button(3)
    index = 0

    def __init__(self):
        # self.but_next.when_pressed = self.next_item
        with canvas(display) as draw:
            draw.text((0,0), "MENU", fill='white')
        self.enc = Encoder.Encoder(5,6, self.next_rot)
        GPIO.add_event_detect(26, GPIO.RISING, callback=self.run_func, bouncetime=200)
        pause()

    def next_rot(self, chan):
        val = self.enc.getValue()
        if self.index < val:
            self.index -= 1
        elif self.index > val:
            self.index += 1
        else:
            self.index = 0

        self.index %= len(self.menu_items)
        text, support_func = self.menu_items[self.index]
        if support_func:
            ret = support_func()
        else:
            ret = None
        with canvas(display) as draw:
            draw.text((0,0), text, fill='white')
            draw.text((10,10), str(ret), fill='white')
        # print('RotEnc value ', str(val))


    def next_item(self):
        self.index = ( self.index + 1 ) % len(self.menu_items)
        text = self.menu_items[self.index]
        print(text)
        with canvas(display) as draw:
            draw.text((0,0), str(text), fill='white')
        
    def run_func(self, chan):
        func = self.menu_funcs[self.index]
        info = func()
        print("function run ", str(func), " on chan ", str(chan))
        if info:
            print(info)
            with canvas(display) as draw:
                draw.text((0,0), str(info), fill='white')


a = Menu()
