import numpy as np
import time

# This program generates random numbers from three different distributions and displays the mean and standard deviation for each. 

g = np.random.normal(size = 1000)

u = np.random.uniform(size = 1000)

r = np.random.randint(0, 500+1, size = 1000)

print("Generating random numbers from Normal, Uniform, and Random Distributions ")
time.sleep(.5)

print("Calculating Mean and Standard Deviation for each distribution")
print()
g_mean = np.mean(g)

g_stdev = np.std(g)

u_mean = np.mean(u)

u_stdev = np.std(u)

r_mean = np.mean(r)

r_stdev = np.std(r)

print(f'Normal Distribution: Mean = {g_mean} Standard Deviation = {g_stdev}')
print()
time.sleep(.5)
print(f'Uniform Distribution: Mean = {u_mean} Standard Deviation = {u_stdev}')
print()
time.sleep(.5)
print(f'Random Distribution: Mean = {r_mean} Standard Deviation = {r_stdev}')



