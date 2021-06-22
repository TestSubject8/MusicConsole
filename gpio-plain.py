from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544, st7735, uc1701x
#from luma.lcd.aux import backlight

serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=9)

display = pcd8544(serial, rotate=2)

def indicate():
    def decor(func):
        led_indicate.on()
        sleep(1)
        led_indicate.off()
        func()
        return
    return decor


menu_items = ['Show devices', 'Switch devices']
menu_funcs = [show_devices, switch_device]
menu_len = len(menu_items)
but_next  = Button(2)
but_select = Button(3)
index = 0

def display_menu():
    global menu_items, index
    print(menu_items[index])
    with canvas(display) as draw:
        draw.text((10,10), menu_items[index], fill='red')

def update_index():
    global index
    index = ( index + 1 ) % menu_len
    display_menu()

def select():
    global index, menu_funcs
    menu_funcs[index]()

but_next.when_pressed = update_index
but_select.when_pressed = select

pause()
