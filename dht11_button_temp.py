import Adafruit_DHT
import RPi.GPIO as gp
import time
sensor=Adafruit_DHT.DHT11
gpio=17
btn=10
humi, temp = Adafruit_DHT.read_retry(sensor, gpio)
gp.setwarnings(False) # Ignore warning for now
gp.setmode(gp.BOARD) # Use physical pin numbering
gp.setup(18,gp.OUT)
gp.setup(btn, gp.IN, pull_up_down=gp.PUD_UP)
print("press button")
while True:
	if (gp.input(btn)==gp.HIGH):
		gp.output(18,True)
		print("Button was pushed!")
		print(humi)
		print(temp)
		time.sleep(0.5)
	else:
		gp.output(18,False)
gp.cleanup()
