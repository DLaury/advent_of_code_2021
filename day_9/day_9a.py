import numpy as np

with open('day_9\input.txt') as f:
    height_map = np.array([list(x) for x in f.read().splitlines()], dtype=np.int32)

def local_minima(array2d):
    padded_array = np.pad(array2d, pad_width=1, mode='constant', constant_values=9)
    padded_array = ((padded_array < np.roll(padded_array,  1, 0)) &
            (padded_array < np.roll(padded_array, -1, 0)) &
            (padded_array < np.roll(padded_array,  1, 1)) &
            (padded_array < np.roll(padded_array, -1, 1)))
    array_mask = padded_array[1:-1, 1:-1]
    return array_mask

print(sum(height_map[local_minima(height_map)]+1))