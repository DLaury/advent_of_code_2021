import numpy as np

with open('day_7\input.txt') as f:
    one = np.array(f.readline().split(','), dtype=np.int32)

def fuel_calc(positions):
    high = np.amax(positions)
    fuel = []
    for x in range(0, high+1):
        difference = np.full_like(positions, x)
        test = sum(abs(one - difference))
        fuel.append(test)
    return min(fuel)

print(fuel_calc(one))