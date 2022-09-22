from gpiozero import Button, LED
from signal import pause
import time
button = Button(15)
led = LED(24)
button.when_pressed = led.on
pause()
