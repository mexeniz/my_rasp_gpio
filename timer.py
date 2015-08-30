from threading import Thread
import time
import RPi.GPIO as GPIO
pinOut = [4,2,3]
threadList = []
def setupGPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

def toggleOutput(pin,pinState):
	if(pinState == 1):
		pinState = 0
	else :
		pinState = 1
	GPIO.output(pin,pinState)
	return pinState

def timer(pin,delay,repeat):
	print "Timer at port " + str(pin) + " : Started!"
	pinState = 0
	while repeat > 0 :
		time.sleep(delay)
		print str(pin) + " : " + str(time.ctime(time.time()))
		pinState = toggleOutput(pin , pinState)
		repeat -= 1
	print "Timer at port " + str(pin) + " : Finished!"
	
def main():
	setupGPIO()
	for pin in pinOut :
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,0)
		print str(pin) + " Config"
		delay = input("Delay :")
		repeat =  input("Repeat :")
		t = Thread(target = timer,args=(pin,delay,repeat))
		threadList.append(t)
	start = raw_input("Press any key to start...")
	for t in threadList :
		t.start()
	
	while(1):
		try:
			x = 0	
		except (KeyboardInterrupt,SystemExit):
			print "STOP!"
			GPIO.cleanup()
			for t in threadList :
				if t.isAlive():
					print "Stop thread"
					t._Thread__stop()
	return
main()
