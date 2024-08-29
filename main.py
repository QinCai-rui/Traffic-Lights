# Imports necessary libraries
from machine import Pin
from picozero import Speaker
from time import sleep
import _thread

# Initialise the three LEDs
LED_RED = Pin(13, Pin.OUT)
LED_YELLOW = Pin(14, Pin.OUT)
LED_GREEN = Pin(15, Pin.OUT)

# Initialise the buzzer
BUZZER = Speaker(17)

# Initialise the button
BUTTON = Pin(16, Pin.IN, Pin.PULL_DOWN)

FACTOR = 1

btn_pressed = False


def test_thr():
    while 1:
        LED_RED.value(1)
        LED_YELLOW.value(1)
        LED_GREEN.value(1)
        sleep(1.5)

def test():
    LED_RED.value(1)
    LED_YELLOW.value(1)
    LED_GREEN.value(1)
    sleep(1.5)
    BUZZER.on()
    sleep(1)
    
    LED_RED.value(0)
    LED_YELLOW.value(0)
    LED_GREEN.value(0)
    BUZZER.off()

def btn_pr_thr():
    global btn_pressed
    while 1:
        if BUTTON.value() == 1:
            btn_pressed = True
        sleep(0.1)

def main():
    global btn_pressed
    while 1:
        if btn_pressed == True:
            sleep(2)
            LED_RED.value(1)
            for i in range(10):
                BUZZER.on()
                sleep(0.04)
                BUZZER.off()
                sleep(0.2)
            btn_pressed = False
        LED_RED.value(1)
        sleep(5)
        LED_YELLOW.value(1)
        sleep(2)
        LED_RED.value(0)
        LED_YELLOW.value(0)
        LED_GREEN.value(1)
        sleep(5)
        LED_GREEN.value(0)
        LED_YELLOW.value(1)
        sleep(5)
        LED_YELLOW.value(0)


if __name__ == '__main__':
    #_thread.start_new_thread(test_thr, ())
    main()
    #test()
