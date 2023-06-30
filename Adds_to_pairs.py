'''This function takes a list, n, and a chosen number, k, as arguments. 
It then checks if any two pairs from the list add up to the chosen number.
If I a pair exists, a set of tuples is returned'''
k = 58
n = [4, 3, 5, 6, 34, 11, 11, 11, 11, 23, 22, 0, 42, 78, 35, 21, 15, 45, 60, 39, 38, 20]

def adds_to_k(n, k):

    compare = set()
    pairs = []
    
# Checking for difference of k minus items in function argument. 
    for i in n:
        if k - i in compare:
            pairs.append((i, k-i)) #If there is a match, the function returns sets of tuple pairs that equal k.
        compare.add(i)
    if len(pairs)>0: #If anything matches criteria, return a set. 
        return set(pairs)
    else:
        print ("No pairs that add to k")


print(adds_to_k(n,k))