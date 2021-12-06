with open('day_3\input.txt') as f:
    bits = [line.strip() for line in f]

totals = [0 for x in range(len(bits[0]))]

for x in bits:
    for pos, bit in enumerate(x):
        if int(bit) == 1:
            totals[pos] += int(bit)
        else:
            totals[pos] -= 1
gamma = int(''.join(['1' if x > 0 else '0' for x in totals]), 2)
epsilon = int(''.join(['1' if x < 0 else '0' for x in totals]), 2)

print("totals: ", totals)
print("gamma: ", gamma)
print("epsilon: ", epsilon)
print("consumption: ", gamma * epsilon)
