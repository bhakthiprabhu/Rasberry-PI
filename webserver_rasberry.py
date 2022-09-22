import RPi.GPIO as GPIO
import os
temp = os.popen(" ").read()
print(temp)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)

try:
    while True:
        user_input = input("Turn LED On or Off with 1 or 0 (Ctrl-C to exit): ")
        if user_input is "1":
            GPIO.output(24,GPIO.HIGH)
            print("LED is on")
        elif user_input is "0":
            GPIO.output(24,GPIO.LOW)
            print("LED is off")
except KeyboardInterrupt:
    GPIO.cleanup()
    print("")
