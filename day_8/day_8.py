with open('day_8\input.txt') as f:
    output = [line.strip().split(' | ')[1].split(' ') for line in f]

combined = sum(output, [])
counts = [x for x in combined if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7]
print(len(counts))