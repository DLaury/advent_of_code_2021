import collections, functools, operator

with open('day_2\input.txt') as f:
    directions = [{line.strip().split(' ')[0]: int(line.strip().split(' ')[1])} for line in f]
aim = 0
horizontal = 0
depth = 0

for x in directions:
    if 'forward' in x:
        horizontal += x.get('forward')
        depth += x.get('forward') * aim
    elif 'up' in x:
        aim -= x.get('up')
    else:
        aim += x.get('down')

print(depth * horizontal)