with open('day_1\input.txt') as f:
    depths = [int(line.strip()) for line in f]
greater = 0
for i, x in enumerate(depths):
    if i == 0:
        pass
    else:
        if depths[i] > depths[i-1]:
            greater += 1
print(greater)