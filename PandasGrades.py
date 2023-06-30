import pandas as pd 
import numpy
import time

# I added a bit to this one as well to make it display nicely. I really enjoy working with Pandas!

a = {'Math' : [80, 89, 93, 66, 84, 85, 74, 64],
'Science' : [94, 76, 88, 78, 88, 92, 60, 85],
'English' : [83, 76, 93, 96, 77, 85, 92, 60],
'History' : [96, 66, 76, 85, 78, 88, 69, 99]}

df = pd.DataFrame(a) #Create dataframe directly from dictionary
# General statistics for the entire dataframe. 
a_std =df.std() #Standard Deviation
b_mean = df.mean() #Mean
c = df.median() #Median


# Math Five Number Summary 
math_min = df['Math'].min()
math_max = df['Math'].max()
math_quantiles=df['Math'].quantile([.25, .75])
math_mean = df['Math'].mean()
math_median = df['Math'].median()

#Science Five Number Summary
science_min = df['Science'].min()
science_max = df['Science'].max()
science_quantiles=df['Science'].quantile([.25, .75])
science_mean = df['Science'].mean()
science_median = df['Science'].median()

# English Five Number Summary 
english_min = df['English'].min()
english_max = df['English'].max()
english_quantiles=df['English'].quantile([.25, .75])
english_mean = df['English'].mean()
english_median = df['English'].median()

#History Five Number Summary 
history_min = df['History'].min()
history_max = df['History'].max()
history_quantiles=df['History'].quantile([.25, .75])
history_mean = df['History'].mean()
history_median = df['History'].median()

#Displaying Dataframe and Five Number Summaries below. 

print("Printing complete dataframe")
time.sleep(1)
print (df)
print()
print("*******")
time.sleep(2)

print(" Standard Deviation and Mean for Each Course ")
time.sleep(1)
print(f'Standard Deviation:')
print(a_std)
print('Mean:')
print(b_mean)
print("*******")
time.sleep(1)



print("Five Number Summaries for Each Course")
print("*******")
time.sleep(1)

print (f'Math Summary: Median: {math_median}, Mean:{math_mean}, Minimum: {math_min}, Maximum: {math_max} 1st and 3rd Quantiles: {math_quantiles}')
print("*******")
time.sleep(1)
print (f'Science Summary: Median: {science_median}, Mean:{science_mean}, Minimum: {science_min}, Maximum: {science_max} 1st and 3rd Quantiles: {science_quantiles}')
print("*******")
time.sleep(1)
print (f'English Summary: Median: {english_median}, Mean:{english_mean}, Minimum: {english_min}, Maximum: {english_max} 1st and 3rd Quantiles: {english_quantiles}')
print("*******")
time.sleep(1)
print (f'History Summary: Median: {history_median}, Mean:{history_mean}, Minimum: {history_min}, Maximum: {history_max} 1st and 3rd Quantiles: {history_quantiles}')
print("*******")