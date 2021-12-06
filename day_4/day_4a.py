with open('day_4\input.txt') as f:
    lines = []
    row = []
    lines.append(list(int(x) for x in f.readline().strip().split(',')))
    f.readline()
    for entry in f:
        if entry == '\n':
            lines.append(row)
            row = []
        else:
            row.append(list(filter(None, entry.strip('  ').strip().split(' '))))
print(lines[1])
