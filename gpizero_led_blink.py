from gpiozero import LED
from time import sleep

led = LED(24)

print("led")
while True:
	led.on()
	print("led on")
	sleep(0.5)
	led.off()
	print("led off")
	sleep(0.5)
