import numpy as np
with open('day_4\input.txt') as f:
    cards = []
    row = []
    numbers = list(int(x) for x in f.readline().strip().split(','))
    f.readline()
    for entry in f:
        if entry == '\n':
            cards.append(np.array(row))
            row = []
        else:
            row.append([int(x) for x in filter(None, entry.strip('  ').strip().split(' '))])
    cards.append(np.array(row))

def bingo_score(numbers, cards):
    start = len(cards[0][0])
    called_nums = numbers[:start]
    while len(cards) > 1:
        for i, card in enumerate(cards):
            for row in card:
                if all(nums in called_nums for nums in row):
                    cards.pop(i)
            for column in card.transpose():
                if all(nums in called_nums for nums in column):
                    cards.pop(i)
        start += 1
        called_nums = numbers[:start]
    return np.sum(cards, where=np.isin(cards, numbers[:start], invert=True)) * numbers[start-1]

print(bingo_score(numbers, cards))