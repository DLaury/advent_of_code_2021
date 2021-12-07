import re

with open('day_5\input.txt') as f:
    lines = [list(map(int, re.split(' -> |,', line.strip()))) for line in f]

for i, points in enumerate(lines):
    if (points[0] != points[2]) & (points[1] != points[3]):
        lines.pop(i)