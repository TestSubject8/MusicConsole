from screen_trial import display_text
import modules.display as display
import Encoder
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

for x in [26]:
    GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def update_disp(channel):
    # display.clear()
    v = enc.getValue()
    print('val is {} on {}'.format(v, channel))
    # with display.canvas(display) as draw:
    #     draw.text((0,0), str(v), fill='white')
    # display.pause()

def update(channel):
    print('updated on', str(channel))

enc = Encoder.Encoder(23, 24, update_disp)

GPIO.add_event_detect(26, GPIO.BOTH, callback=update, bouncetime=200)
print("Done setup")

# display.pause()

while(True):
    if GPIO.input(26):
        print("ON")
        # with display.canvas(display) as draw:
            # draw.text((0,0), "ON", fill='white')
    else:
        print("OFF")
        # with display.canvas(display) as draw:
            # draw.text((0,0), "OFF", fill='white')
    time.sleep(3)

