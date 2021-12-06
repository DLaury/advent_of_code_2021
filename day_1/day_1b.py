with open('day_1\input.txt') as f:
    depths = [int(line.strip()) for line in f]
greater = 0
for i, x in enumerate(depths):
    if i == 0:
        a = depths[i] + depths[i+1] + depths[i+2]
    elif i >= len(depths) - 2:
        break
    else:
        a = depths[i-1] + depths[i] + depths[i+1]
        b = depths[i] + depths[i+1] + depths[i+2]
        if b > a:
            greater += 1
print(greater)