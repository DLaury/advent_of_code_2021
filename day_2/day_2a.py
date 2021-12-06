import collections, functools, operator

with open('day_2\input.txt') as f:
    directions = [{line.strip().split(' ')[0]: int(line.strip().split(' ')[1])} for line in f]
  
# sum the values with same keys
result = dict(functools.reduce(operator.add,
         map(collections.Counter, directions)))

result['up'] = result.get('up') * -1

position = (result.get('up') + result.get('down')) * result.get('forward')

print(position)
