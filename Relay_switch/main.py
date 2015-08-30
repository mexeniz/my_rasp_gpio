#!/usr/bin/env python
import threading
import time , datetime
import RPi.GPIO as GPIO

class Relay_switch(object):
	def __init__(self,name,rs_port,repeat,ac_length,duration,is_infinite):
		self.name = name
		self.rs_port = rs_port
		self.repeat = repeat
		self.ac_length = ac_length
		self.duration = duration
		self.created_time = time.time()
		self.last_runtime = time.time()
		self.next_runtime = self.last_runtime + repeat
		if (duration < 0):
			self.is_infinite = True 
		else :
			self.is_infinite = is_infinite
	def time_logging(self):
		return datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M:%S%p")
    
	def setup(self):
		print ('Set up GPIO port : {} at Thread--{} @{}'.format(self.rs_port , self.name , self.time_logging())) 
		GPIO.setup(self.rs_port , GPIO.OUT)
		self.thread = threading.Thread(target=self.run)
		self.thread.start()
        
	def activate(self):
		#print( 'Toggle port {} up @{}'.format( self.rs_port , self.time_logging())
		GPIO.output(self.rs_port , 1)
		time.sleep(self.ac_length)
		#print( 'Toggle port {} down @{}'.format(self.rs_port, self.time_logging() ))
		GPIO.output(self.rs_port , 0)
   	
	def run(self):
       		 ##Thread targets this function##
        
        	# last_runtime = time.time()
        	# next_runtime = last_runtime + self.repeat
		is_finished = False
		while not is_finished :
			##Thread loop
			now = time.time()
			if (not self.is_infinite and now > self.created_time + self.duration):
                		is_finished = True
			elif now > self.next_runtime :
				print('Activate port {}'.format(self.rs_port))
				self.last_runtime = self.next_runtime
				self.next_runtime = self.next_runtime + self.repeat
				self.activate()
		print('Kill Thread--{} , port {} is freed. @{}'.format(self.name , self.rs_port , self.time_logging()))
		pass

def init():
	GPIO.setmode(GPIO.BCM)
def main():
    
	init()
	my_thread = Relay_switch("Mmarcl",4,4,0.5,60,False)
	my_thread.setup()
	
	my_thread2 = Relay_switch("Mexeniz",2,10,3,70,False)
	my_thread2.setup()

    
    #my_thread3 = Relay_switch("Woodie",41,8,5,20,True)
    #my_thread3.setup()
    
	time.sleep(20)
	my_thread.duration = 90
    
if __name__ == '__main__' :
	main()
