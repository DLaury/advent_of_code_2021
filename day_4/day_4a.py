import numpy as np
with open('day_4\input.txt') as f:
    cards = []
    row = []
    numbers = list(int(x) for x in f.readline().strip().split(','))
    f.readline()
    for entry in f:
        if entry == '\n':
            cards.append(row)
            row = []
        else:
            row.append(list(filter(None, entry.strip('  ').strip().split(' '))))
    cards.append(row)
print("numbers: ", numbers)
for i, x in enumerate(cards):
    print(np.matrix(x), f" - card {i}")
