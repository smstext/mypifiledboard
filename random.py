from gpiozero import PWMLED
from time import sleep
import random
import threading

white = PWMLED(23)
snowflakes = PWMLED(18)
colours = PWMLED(24)

LIGHTS = [white,snowflakes,colours]

def gentle(lights):
    for x in range(1,100):
        lights.value = x/100
        sleep(0.05)

def randomblink(lights): 
    lights.blink(random.randint(1,10)/10,random.randint(1,10)/10,10,False)

def sequence(lights):
    while True:
        print('gentle')
        gentle(lights)
        print('sleep')
        sleep(random.randint(1,10)/10)
        print('blink')
        randomblink(lights)
        print('sleep')
        sleep(random.randint(1,10)/10)
        print('on')
        lights.on()
        print('sleep')
        sleep(random.randint(1,10))

for i in LIGHTS:
    t = threading.Thread(target=sequence, args=(i,))
    t.start()

