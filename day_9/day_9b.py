import numpy as np
from skimage.segmentation import flood_fill
from numpy.lib.arraypad import pad

with open('day_9\input.txt') as f:
    height_map = np.array([list(x) for x in f.read().splitlines()], dtype=np.int32)

def local_minima(array2d):
    padded_array = np.pad(array2d, pad_width=1, mode='constant', constant_values=9)
    min_mask = ((padded_array < np.roll(padded_array,  1, 0)) &
            (padded_array < np.roll(padded_array, -1, 0)) &
            (padded_array < np.roll(padded_array,  1, 1)) &
            (padded_array < np.roll(padded_array, -1, 1)))
    results = np.where(min_mask)
    padded_array[np.where(padded_array != 9)] = 0
    min_list = list(zip(results[0], results[1]))
    return min_list, padded_array

min_q, padded_array = local_minima(height_map)

count = 10
for x in min_q:
    flood_fill(padded_array, x, count, connectivity=1, in_place=True)
    count += 1

unique, counts = np.unique(padded_array, return_counts = True)
totals = dict(zip(unique, counts))
totals.pop(9)
value = np.prod(sorted(totals.values())[-3:])
print(value)