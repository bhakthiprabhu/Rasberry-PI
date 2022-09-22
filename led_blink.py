import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setup(21,gp.OUT)
while True:
	gp.output(21,True)
	time.sleep(0.5)
	gp.output(21,False)
	time.sleep(0.5)

