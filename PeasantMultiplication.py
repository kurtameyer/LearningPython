'''This is a rudimentary implementation of the Ancient Egyptian or 
Peasant multiplication algorithm. This is meant to show a basic
understanding of loops, lists, dictionaries, and, of course math 🧮'''

n1 = int(input("Please enter a multiplicand greater than 0:  "))
n2 = int(input ("Please enter a multiplier greater than 0:  "))

#Two lists with initial entries from user input variables. 
list1 = [n1]
list2 = [n2]

#Setting up counter 
count = 0

#While loop cycles through math for halved numbers and appends floor divided answers to list1
while n1 > 1:
   n1 = n1 // 2
   count +=1
   list1.append(n1)
  

#For loop to cycle through math append doubled values to list2.  
for i in range (0, count):#Range dependent on counter 
   n2 = n2*2
   list2.append(n2)

#Create dictionary with halved numbers as keys and doubled numbers as values
alt_math = dict(zip(list1, list2))


#Dictionary comprehension removes odd numbered keys 
alt_math = {key: alt_math[key] for key in alt_math if key % 2 != 0}

#Final answer calculated by adding all values 
answer = sum(alt_math.values())

print(answer)