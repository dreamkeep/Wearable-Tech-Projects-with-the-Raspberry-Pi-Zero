#!/usr/bin/python3

import scrollphathd as shd #import our Scroll pHAT library
from time import sleep #import sleep from the time library

shd.clear() #clear any LEDs which are already lit
shd.show() #must call show after clear
shd.write_string("Hello, my name is Jon Witts!     ", brightness=0.25) 
#The message to scroll with 5 spaces at the end
#the brightness sets the LEDs to 25%

while True: #We start a while loop which goes on forever
   shd.show() #Show message on the LEDs
   shd.scroll(1) #Scroll along the x-axis 1 pixel at a time
   sleep(0.05) #Wait for 0.05 of a second before returning
               #to the start of the loop
