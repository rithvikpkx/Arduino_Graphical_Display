from microbit import *

import random

#11.9
#Create a row of pixels lit up on brightness 5
wall = Image("55555:00000:00000:00000:00000") # ← New

#Create empty image called field
field = Image()

#11.10
#Set variable i_wall to 0 to create empty wall
i_wall = 0

#11.12
#Create variables to initialize player at starting coordinates (2,3)
player_x = 2
player_y = 3

#11.13
#Set delay for how often the player can scroll to another pixel to 500 milliseconds
scrollMs = 500

#Set delay between each scroll to sum of scrollMs and running time of the program
nextScroll = running_time() + scrollMs

#11.14
#Set player score to 0 at beginning of the game
score = 0

#Infinitely loop indented code
while True:
      
     #Checks for collision between wall and player
     #If a collision occurs, end game by breaking while loop
	if field.get_pixel(player_x, player_y):
    		break
     
     #11.12
     #Establish controls for player movement with button inputs
     #Decrement player_x value by 1 when button a pressed and player_x value greater than 0
     #Increment player_x value by 1 when button b pressed and player_x value less than 4
	if button_a.was_pressed() and player_x > 0:
    		player_x = player_x - 1
   	 
	if button_b.was_pressed and player_x < 4:
    		player_x = player_x + 1
     
     #Display player pixel at player coordinates with full brightness 9
	display.set_pixel(player_x, player_x, 9)
    
     #11.13
     #Conditional if statement to check if program run time is greater than nextScroll value
	if running_time() > nextScroll:

           #Shift down the field by 1 to move closer to player
    		field = field.shift_down(1)

           #Increment value of nextScroll by value of scrollMs
    		nextScroll = nextScroll + scrollMs
   	 
           #11.10
           #Increment value of i_wall by 1
    		i_wall = i_wall + 1
   	 
           #Conditional if statement to check if i_wall is equal to 3
           #If i_wall is equal to 3, then set i_wall to 0
    		if i_wall == 3:
        		i_wall = 0
       	 
                #Increment value of field by value of wall
        		field = field + wall
       	 
                #11.11
                #Create new variable gate that has a random value from 0 - 5
        		gate = random.randrange(5)

                #Initialize gate at coordinates (0, 0) on the field
        		field.set_pixel(gate, 0, 0)
       	 
                #11.14
                #Increment value of score by 1
        		score = score + 1
       	 
                #11.13
                #Conditional if statement to check if value of scrollMs exceeds 200
                #If value exceeds 200, run indented code
        		if scrollMs > 200:

                      #Decrement value of scrollMs by 5
            		scrollMs = scrollMs - 5
    
     #Show field on display 	 
    	display.show(field)

#11.14
#Show sad image on display
display.show(Image.SAD)

#Wait for 500 milliseconds before moving on
sleep(500)

#Scroll converted string value of score across microbit screen forever and end the code
display.scroll(str(score), loop=True, wait=False)
