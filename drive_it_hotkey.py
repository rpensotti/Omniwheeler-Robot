# import curses and GPIO
import time
import sys
import RPi.GPIO as GPIO
import os
import keyboard

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

def command(cmd):
    global duty

    # Key 'r' rotate Omniweeler clockwise
    if cmd == "rotate_c":
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(13, False)
        GPIO.output(15, True)
        GPIO.output(19, False)
        GPIO.output(21, True)
        GPIO.output(23, True)
        GPIO.output(29, False)

    # Key 'l' rotate Omniweeler counterclockwise
    elif cmd == "rotate_cc":
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(13, True)
        GPIO.output(15, False)
        GPIO.output(19, True)
        GPIO.output(21, False)
        GPIO.output(23, False)
        GPIO.output(29, True)


    # Key UP  Omniweeler moves forward square
    elif cmd == "up":
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, False)
        GPIO.output(19, True)
        GPIO.output(21, False)
        GPIO.output(23, True)
        GPIO.output(29, False)

    # Key DOWN  Omniweeler moves backwards square
    elif cmd == "down":
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, True)
        GPIO.output(19, False)
        GPIO.output(21, True)
        GPIO.output(23, False)
        GPIO.output(29, True)

    # Key RIGHT  Omniweeler moves right square
    elif cmd == "right":
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, True)
        GPIO.output(19, True)
        GPIO.output(21, False)
        GPIO.output(23, True)
        GPIO.output(29, False)



    # Key LEFT  Omniweeler moves left square
    elif cmd == "left":
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, False)
        GPIO.output(19, False)
        GPIO.output(21, True)
        GPIO.output(23, False)
        GPIO.output(29, True)


    # Key 't'  Omniweeler moves North East
    elif cmd == "northeast":
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(19, True)
        GPIO.output(21, False)
        GPIO.output(23, True)
        GPIO.output(29, False)

    # Key 'e'  Omniweeler moves North West
    elif cmd == "northwest":
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, False)
        GPIO.output(19, False)
        GPIO.output(21, False)
        GPIO.output(23, False)
        GPIO.output(29, False)

    # Key 'b'  Omniweeler moves South  East
    elif cmd == "southeast":
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, True)
        GPIO.output(19, False)
        GPIO.output(21, False)
        GPIO.output(23, False)
        GPIO.output(29, False)

    # Key 'c'  Omniweeler moves South West
    elif cmd == "southwest":
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(19, False)
        GPIO.output(21, True)
        GPIO.output(23, False)
        GPIO.output(29, True)

    # Key 's'  Omniweeler full stop
    elif cmd == "stop":
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(19, False)
        GPIO.output(21, False)
        GPIO.output(23, False)
        GPIO.output(29, False)
    # Key 'v'  Start Pi Camera video Capture

    elif cmd == "video_on":
        os.system('./vc_start.sh')
    elif cmd == "video_off":
        os.system('./vc_stop.sh')

    # Key 'p'  Start camera servo sweep
    elif cmd == "servo_sweep":
        setAllDutyCycle(7.5)
        time.sleep(1)
        setAllDutyCycle(12.5)
        time.sleep(1)
        setAllDutyCycle(2.5)
        time.sleep(1)
    elif cmd == "duty+":
        duty += 5
        duty = min(duty, 100.)
        print duty
        setAllDutyCycle(duty)
    elif cmd == "duty-":
        duty -= 5
        duty = max(duty, 0.)
        print duty
        setAllDutyCycle(duty)


keyboard.add_hotkey("left", command, args=("left",))
keyboard.add_hotkey("right", command, args=("right",))
keyboard.add_hotkey("up", command, args=("up",))
keyboard.add_hotkey("down", command, args=("down",))
keyboard.add_hotkey("s", command, args=("stop",))
keyboard.add_hotkey("equal", command, args=("duty+",))
keyboard.add_hotkey("minus", command, args=("duty-",))

keyboard.add_hotkey("t", command, args=("northeast",))
keyboard.add_hotkey("e", command, args=("northwest",))
keyboard.add_hotkey("b", command, args=("southeast",))
keyboard.add_hotkey("c", command, args=("southwest",))

keyboard.add_hotkey("r", command, args=("rotate_c",))
keyboard.add_hotkey("l", command, args=("rotate_cc",))

keyboard.add_hotkey("p", command, args=("servo_sweep",))



keyboard.wait('esc')
GPIO.cleanup()
