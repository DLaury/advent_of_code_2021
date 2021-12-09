import numpy as np
with open('day_6\input.txt') as f:
    ages = np.array(f.readline().split(',')).astype(np.int32)

def fish(timers, days):
    for day in range(0, days):
        timers = timers - 1
        num_zeros = len(timers[timers==-1])
        timers = np.where(timers == -1, 6, timers)
        zeros = (np.array([8] * num_zeros,  dtype=int))
        timers = np.concatenate((timers, zeros), axis=None)
    print(len(timers))

fish(ages, 80)