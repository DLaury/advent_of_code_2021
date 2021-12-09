import re
import numpy as np

with open('day_5\input.txt') as f:
    coords = [list(map(int, re.split(' -> |,', line.strip()))) for line in f]

x_base = 0
y_base = 0
lines = []
for i, points in enumerate(coords):
    x1, y1, x2, y2 = points
    if x1 == x2:
        if y1 == y2:
            lines.append([x1, y1])
        elif y2 < y1:
            for y in range(y2, y1+1):
                lines.append([x1, y])
        else:
            for y in range(y1, y2+1):
                lines.append([x1, y])
    elif y1 == y2:
        if x2 < x1:
            for x in range(x2, x1+1):
                lines.append([x, y1])
        else:
            for x in range(x1, x2+1):
                lines.append([x, y1])
    else:
        if x1 > x2:
            for start in range(x2, x1+1):
                if y1 >= y2:
                    lines.append([x2, y2])
                    y2+=1
                else:
                    lines.append([x2, y2])
                    y2-=1
                x2+=1
        else:
            for start in range(x1, x2+1):
                if y1 >= y2:
                    lines.append([x1, y1])
                    y1-=1
                else:
                    lines.append([x1, y1])
                    y1+=1
                x1+=1
    max_x = max(x1, x2)
    max_y = max(y1, y2)
    if max_x > x_base:
        x_base = max_x
    if max_y > y_base:
        y_base = max_y

grid = np.zeros((x_base+1, y_base+1), dtype=int)

for point in lines:
    grid[point[0]][point[1]] += 1

more_than_1 = grid > 1
print(more_than_1.sum())