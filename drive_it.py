# import curses and GPIO
import curses
import time
import RPi.GPIO as GPIO
import os

# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

p1 = GPIO.PWM(32, 50)
p2 = GPIO.PWM(36, 50)
p3 = GPIO.PWM(38, 50)
p4 = GPIO.PWM(40, 50)

duty = 50
for p in [p1, p2, p3, p4]:
    p.start(duty)


def setAllDutyCycle(d):
    for p in [p1, p2, p3, p4]:
        p.ChangeDutyCycle(d)


setAllDutyCycle(duty)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
# curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break

        # Key 'r' rotate Omniweeler clockwise
        elif char == ord('r'):
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, True)
            GPIO.output(19, False)
            GPIO.output(21, True)
            GPIO.output(23, True)
            GPIO.output(29, False)

        # Key 'l' rotate Omniweeler counterclockwise
        elif char == ord('l'):
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, True)
            GPIO.output(15, False)
            GPIO.output(19, True)
            GPIO.output(21, False)
            GPIO.output(23, False)
            GPIO.output(29, True)


        # Key UP  Omniweeler moves forward square
        elif char == curses.KEY_UP:
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(15, False)
            GPIO.output(19, True)
            GPIO.output(21, False)
            GPIO.output(23, True)
            GPIO.output(29, False)

        # Key DOWN  Omniweeler moves backwards square
        elif char == curses.KEY_DOWN:
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, True)
            GPIO.output(19, False)
            GPIO.output(21, True)
            GPIO.output(23, False)
            GPIO.output(29, True)

        # Key RIGHT  Omniweeler moves right square
        elif char == curses.KEY_RIGHT:
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, True)
            GPIO.output(19, True)
            GPIO.output(21, False)
            GPIO.output(23, True)
            GPIO.output(29, False)



        # Key LEFT  Omniweeler moves left square
        elif char == curses.KEY_LEFT:
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(15, False)
            GPIO.output(19, False)
            GPIO.output(21, True)
            GPIO.output(23, False)
            GPIO.output(29, True)


        # Key 't'  Omniweeler moves North East
        elif char == ord('t'):
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(19, True)
            GPIO.output(21, False)
            GPIO.output(23, True)
            GPIO.output(29, False)

        # Key 'e'  Omniweeler moves North West
        elif char == ord('e'):
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(15, False)
            GPIO.output(19, False)
            GPIO.output(21, False)
            GPIO.output(23, False)
            GPIO.output(29, False)

        # Key 'b'  Omniweeler moves South  East
        elif char == ord('b'):
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, True)
            GPIO.output(19, False)
            GPIO.output(21, False)
            GPIO.output(23, False)
            GPIO.output(29, False)

        # Key 'c'  Omniweeler moves South West
        elif char == ord('c'):
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(19, False)
            GPIO.output(21, True)
            GPIO.output(23, False)
            GPIO.output(29, True)

        # Key 's'  Omniweeler full stop

        elif char == ord('s'):
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(19, False)
            GPIO.output(21, False)
            GPIO.output(23, False)
            GPIO.output(29, False)
        # Key 'v'  Start Pi Camera video Capture

        elif char == ord('v'):
            os.system('./vc_start.sh')
        elif char == ord('n'):
            os.system('./vc_stop.sh')
        # Key 'p'  Start camera servo sweep

        elif char == ord('p'):
            setAllDutyCycle(7.5)
            time.sleep(1)
            setAllDutyCycle(12.5)
            time.sleep(1)
            setAllDutyCycle(2.5)
            time.sleep(1)
        elif char == ord('='):
            duty += 5
            duty = min(duty, 100.)
            print duty
            setAllDutyCycle(duty)
        elif char == ord('-'):
            duty -= 5
            duty = max(duty, 0.)
            print duty
            setAllDutyCycle(duty)


finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
