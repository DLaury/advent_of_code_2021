import numpy as np

with open('day_7\input.txt') as f:
    one = np.array(f.readline().split(','), dtype=np.int32)

def fuel_calc(positions):

    high = np.amax(positions)
    fuel = []
    for x in range(0, high+1):
        difference = np.full_like(positions, x)
        test = abs(one - difference)
        fuel.append(sum(map(lambda x: sum(range(1,x+1)), test)))
    print(min(fuel))

fuel_calc(one)