#Import all the libraries
import RPi.GPIO as GPIO
import time
from pubnub import Pubnub
 
# Initialize the Pubnub Keys 
pub_key = "***************************"
sub_key = "************************"
 
fan1 = 3         #define pin of RPi on which you want to take output
fan2 = 5
 
def init():          #initalize the pubnub keys and start subscribing
 
 global pubnub    #Pubnub Initialization
 gpio.setmode(gpio.BOARD)
 gpio.setwarnings(False)
 gpio.setup(fan1,gpio.OUT)
 gpio.setup(fan2,gpio.OUT)
 gpio.output(fan1, False)
 gpio.output(fan2, False)
 pubnub = Pubnub(publish_key=pub_key,subscribe_key=sub_key)
 pubnub.subscribe(channels='alexaTrigger', callback=callback, error=callback, reconnect=reconnect, disconnect=disconnect)
 
 
def control_alexa(controlCommand):          #this function control Aalexa, commands received and action performed
 if "trigger" in controlCommand:
  if(controlCommand["trigger"] == "fan" and controlCommand["status"] == 1):
   gpio.output(fan1, True)
   gpio.output(fan2, False)
   print "fan is on"
  else:
   gpio.output(fan1, False)
   gpio.output(fan2, False)
   print "fan is off"
 else:
  pass
 
 
 
def callback(message, channel):        #this function waits for the message from the alexatrigger channel
 if "requester" in message:
  control_alexa(message)
 else:
  pass
 
 
def error(message):                    #if there is error in the channel,print the  error
 print("ERROR : " + str(message))
 
 
def reconnect(message):                #responds if server connects with pubnub
 print("RECONNECTED")
 
 
def disconnect(message):               #responds if server disconnects with pubnub
 print("DISCONNECTED")
 
 
if __name__ == '__main__':
 init()                    #Initialize the Script
