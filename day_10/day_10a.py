import re

with open('day_10\input.txt') as f:
    syntax = [list(x.strip()) for x in f]

close = [')',']','}','>']
close_re = r'[\]}\)>]'
char_dict = {')': '(', ']': '[', '}': '{', '>': '<'}
val_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = []

def check_for_closed(line):
    pair_removed = False
    for i, char in enumerate(line):
        if char in close:
            if line[i-1] == char_dict[char]:
                line.pop(i)
                line.pop(i-1)
                # print(''.join(line))
                pair_removed = True       
    if pair_removed == True:
        check_for_closed(line)
    if any(i in line for i in close):
        return re.search(close_re, ''.join(line)).group()
    else:
        return None

for syn in syntax:
    temp = check_for_closed(syn)
    if temp:
        total.append(val_dict[temp])

print(sum(total))