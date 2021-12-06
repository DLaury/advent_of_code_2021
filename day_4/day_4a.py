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
    running = True
    while running:
        for card in cards:
            for row in card:
                if all(nums in called_nums for nums in row):
                    return np.sum(card, where=np.isin(card, numbers[:start], invert=True)) * numbers[start-1]
            for column in card.transpose():
                if all(nums in called_nums for nums in column):
                    return np.sum(card, where=np.isin(card, numbers[:start], invert=True)) * numbers[start-1]
        start += 1
        called_nums = numbers[:start]

print(bingo_score(numbers, cards))