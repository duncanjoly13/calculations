# authors: Duncan Joly, Kieran Musser
# some code from user4511836 and Vincent on stackoverflow
# date: 2/22/2022
# requirements: alive_progress

# import modules
import time
from math import *
from alive_progress import alive_bar

# set number of iterations
n = 2400000000

"""define approximation function
params:
    int num_iterations is number of iterations
    boolean progressBar should be set to True in order to display a progress bar
        if progressBar is false it will print out updates every 10th of a percent of total progress"""
def pi_approx(num_iterations, progressBar):
    # unsure what these do - from stackexchange
    k = 3.0
    s = 1.0

    # check if should display progress bar
    if progressBar:
        # progress bar parameters - total length is n/100
        with alive_bar(24000000, spinner='fish2', title="completion") as bar:
            # loop to calculate Taylor series n times
            for i in range(num_iterations):
                s = s-((1/k) * (-1)**i)
                k += 2
                # updates progress bar
                if i%(n/100) == 0:
                    bar()
        # final return value
        return 4 * s

    # if no progress bar
    else:
        # loop to calculate Taylor series n times
        for i in range(num_iterations):
            s = s-((1/k) * (-1)**i)
            k += 2
            if i%(n/1000) == 0:
                # print updates every 10th of a percent
                print(str(i*100/n)+" percent done: "+str(4*s))
        # final return value
        return 4 * s

# demo
print(pi_approx(n, False))
