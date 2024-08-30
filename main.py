"""
/***************************************************************
 *                                                             *
 *                    GNU GENERAL PUBLIC LICENSE               *
 *                       Version 3, 29 June 2007               *
 *                                                             *
 *  This program is free software: you can redistribute it and *
 *  or modify it under the terms of the GNU General Public     *
 *  License as published by the Free Software Foundation,      *
 *  either version 3 of the License, or (at your option) any   *
 *  later version.                                             *
 *                                                             *
 *  This program is distributed in the hope that it will be    *
 *  useful, but WITHOUT ANY WARRANTY; without even the implied *
 *  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR    *
 *  PURPOSE. See the GNU General Public License for more       *
 *  details.                                                   *
 *                                                             *
 *  You should have received a copy of the GNU General Public  *
 *  License along with this program. If not, see               *
 *  <https://www.gnu.org/licenses/>.                           *
 *                                                             *
 ***************************************************************/
"""

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

# This block of code is useless as _thread is not working
'''
def test_thr():
    while 1:
        LED_RED.value(1)
        LED_YELLOW.value(1)
        LED_GREEN.value(1)
        sleep(1.5)
'''

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

# This block of code is useless as _thread is not working
'''
def btn_pr_thr():
    global btn_pressed
    while 1:
        if BUTTON.value() == 1:
            btn_pressed = True
        sleep(0.1)
'''

def main():
    #global btn_pressed
    while 1:
        '''
        if btn_pressed == True:
            sleep(2)
            LED_RED.value(1)
            for i in range(10):
                BUZZER.on()
                sleep(0.04)
                BUZZER.off()
                sleep(0.2)
            btn_pressed = False
        '''
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
    # Uncommenting this line would cause the program to break
    #_thread.start_new_thread(test_thr, ())
    main()
    #test()
