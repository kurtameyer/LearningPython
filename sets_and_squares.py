
'''Function uses set comprehension to generate a set of tuple pairs with all integers
between 1 and specified input fulfilling the following criteria: a) 1st number is square of the second
b)square is divisible by 3'''

choice = int(input("What would you like the high number to be?" )) #Get high number from user and store as integer variable. 

the_set = {*range(1, choice+1)} #Creating set between 1 and specified number
def set_comp (lst): 
    li = [] #Empty list 
    for i in the_set:
        if (i**2)%3==0: #Checking set contents
            li.append((i, i**2)) #If set contents match append list
    return set(li)

print (set_comp(the_set)) 