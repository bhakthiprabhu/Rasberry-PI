import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
print("dht started")
gpio=17 #BCM mode so pin 11 in rasberry pi and gpio is 17  
#If BOARD mode pin 11 and  gpio is 17
humidity, temp = Adafruit_DHT.read_retry(sensor, gpio)
print("humidity and temperature")
print(humidity)
print(temp)
