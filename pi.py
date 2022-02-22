from math import *
# import numpy as np

n = 2400000000
x = 1
series = []

def pi_approx(num_iterations):
    k = 3.0
    s = 1.0

    for i in range(num_iterations):
        s = s-((1/k) * (-1)**i)
        k += 2
        if i%100000 == 0:
            print(str(i)+"th calculation: "+str(4*s))
            
    return 4 * s

print(pi_approx(n))
