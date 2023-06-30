

import sys
import time 
import matplotlib.pyplot as plt

print ('''The Collatz Sequence is mathmatically unproven yet never disproven. 
This program will take any number provided by the user and
apply the following math operations: 

If the number is even, the next number will be the number halved. 

If the number is odd, the next number will be that number multiplied by 3 and 1 will be added. 

The sequence terminates when it reaches 1. This program will print the entire sequence

and then produce a graph detailing the progression of the Collatz sequence.''') 

print ("Enter a starting number greater than 0 - or QUIT to exit:")
# User input
response = (input('> '))
# Casting user input to integer


if not response.isdecimal() or response == '0': #Check whether input is a word or 0
    print ("You must enter an integer greater than 0.")
    sys.exit()


x = int(response)# Casting user input to integer

#print (f'{x}')
lst = []
xlst = []

while x !=1: #As long as x isn't 1...
 
    if x%2 == 0: #When x is even
        x = x//2 #Divide by 2
        
    else: # When x is odd
        x = (3 * x) + 1 #3x+1
    
    lst.append(x)
    xlst.append(len(lst))
    print (f' {str(x)}') #Print the progression of numbers
    time.sleep(.2)
    print ()

#Generate graph of the Collatz sequence. 

plt.plot(xlst, lst) #Plot result against length of list 

plt.title("Collatz Sequence Progression") #Graph title

plt.xlabel("Sequence Number") #Label X as "Angle"

plt.ylabel("Result") #Label Y as "Sin and Cos"

plt.grid(color = "pink") #Provide grid 

plt.show() #Display graph







