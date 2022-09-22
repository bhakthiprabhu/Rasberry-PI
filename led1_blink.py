import RPi.GPIO as gp
import time
gp.setmode(gp.BOARD)
gp.setup(40,gp.OUT)
while True:
	gp.output(40,True)
	time.sleep(0.5)
	gp.output(40,False)
	time.sleep(0.5)

