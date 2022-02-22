from math import *
#import numpy as np

n= 200000000
x= 1
series = []

def pi_approx(num_iterations):
    k = 3.0
    s = 1.0

    for i in range(num_iterations):
        s = s-((1/k) * (-1)**i)
        k += 2
        if i%10000 == 0:
            print(4*s)

    return 4 * s

print(pi_approx(n))
