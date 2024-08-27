# Imports necessary libraries
from machine import Pin
from picozero import Speaker
from time import sleep

# Initialise the three LEDs
LED_RED = Pin(13, Pin.OUT)
LED_YELLOW = Pin(14, Pin.OUT)
LED_GREEN = Pin(15, Pin.OUT)

# Initialise the buzzer
BUZZER = Speaker(17)

# Initialise the button
BUTTON = Pin(16, Pin.IN, Pin.PULL_DOWN)


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

if __name__ == '__main__':
    test()
