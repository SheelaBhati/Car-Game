#####################################
#                                   #
# File:		CarGame.py              #
# Project:	Car Game by inkoop      #
#                                   #
# Author:	Sheela Bhati            #
# Date: 	Aug 26th, 2019          #
#                                   #
#####################################

################
#	Library    #
################
import random		
# this library is used to generate random number 
# API used: randrange(range_start <including parameter>, range_end <excluding parameter>, min_diffrance)

################
#	Variables  #
################
petrolPump = [0]*5
shortcut = [[0] * 2] * 5 # index 0 indicates source, index 1 indicates Destination
pits = [0]*3


#####################################################
#	Function Name: 	init                            #
#	Purpose:		to intialize the code variables #
#	input:			not any                         #
#	output:			not any                         #
#####################################################
def init():
	# Petrol Pump Assignment
	print ("Petrol pumps generated at ", end =" ")
	for i in range(len(petrolPump)):
		petrolPump[i] = random.randrange(1, 100, 1)
		print(petrolPump[i], end =" ")
	print("")
	
	# Pits Assignment
	print ("Pits generated at ", end =" ")
	for i in range(len(pits)):
		while True: 
			pits[i] = random.randrange(1, 100, 1)
			if(pits[i] not in petrolPump):
				break
		print(pits[i], end =" ")
	print("")
	
	# Shortcut Assignment
	print ("Shotcuts generated at")
	for i in range(len(shortcut)):
		#Source
		shortcut[i][0] = random.randrange(1, 100, 1)
		#Destination
		while True:
			step = random.randrange(-10, 11, 1)
			shortcut[i][1] = shortcut[i][0]+ step
			if(shortcut[i][1]>0 and shortcut[i][1]<=100):
				break
		if(step>0):
			print (str(shortcut[i][0])+" ( "+ str(step) + " Steps forward )")
		else:
			print (str(shortcut[i][0])+" ( "+ str(step) + " Steps backwards )")
			
######################################################################
#	Function Name: 	letsGo                                           #
#	Purpose:		this function moves the car and                  #
#					displays the current status with steps taken     #
#	input:			not any                                          #
#	output:			not any                                          #
######################################################################
def letsGo():
	# move variable holds count steps car has taken so far
	move = 0
	# curr variable holds current km of car
	curr = 0
	# petrol variable holds remaining petrol in car
	petrol = 30
	while True:
		# increment of move
		move+=1
		
		# take next step
		step = random.randrange(1, 6, 1)
		curr += step
		petrol -= step
		print ("Move " + str(move)+" - Car at "+ str(curr)+" petrol remaining " + str(petrol), end =" ")
		
		# check if petrol is empty
		if(petrol<0):
			print(", game over")
			return
		
		# check if is there a petrol pump
		if(curr in petrolPump):
			petrol += 20
			print(", petrol refilled", end =" ")	

		# check if car reached to destination
		if(curr>=100):
			print (", Destination Reached")
			return
			
		# take shortcut if any
		for i in range(len(shortcut)):
			if(curr==shortcut[i][0]):	
				print(", shortcut to " + str(shortcut[i][1]), end =" ")
				curr = shortcut[i][1]

		# check if car went to a pit
		for pts in pits:
			if(curr==pts):
				print(", Crashed into a pit, game over")
				return
		print()

		
if __name__== "__main__":
	# intialize the variables
	init()
	# lets drive the car
	letsGo()
	
