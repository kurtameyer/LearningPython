prime_num = []
for i in range (2, 30):
     count = 0
     for j in range (2, i//2+1):
         if (i % j == 0):
             count = count + 1
             break
     if (count == 0 and i !=1):
         prime_num.append(i)