signal = []
display = []
final = []

with open('day_8\input.txt') as f:
    for line in f:
        two_lines = line.strip().split(' | ',)
        signal.append(two_lines[0].split(' '))
        display.append(two_lines[1].split(' '))

sorted_signal = [[''.join(sorted(b)) for b in a] for a in signal]
sorted_display = [[''.join(sorted(c)) for c in d] for d in display]

for i, sigs in enumerate(sorted_signal):
    poss = {2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: []}
    totals = {}
    for sig in sigs:
        poss[len(sig)].append(sig)
        if len(sig) == 2:
            totals[sig] = '1'
        elif len(sig) == 3:
            totals[sig] = '7'
        elif len(sig) == 4:
            totals[sig] = '4'
        elif len(sig) == 7:
            totals[sig] = '8'
        
    for x in poss[6]:
        if (len(set(poss[3][0]) - set(x)) == 0)  & (len(set(poss[4][0]) - set(x)) == 0):
            totals[x] = '9'
            for y in poss[5]:
                if len(set(x)-set(y)) == 2:
                    totals[y] = '2'
        elif len(set(poss[3][0]) - set(x)) == 0:
            totals[x] = '0'
        else:
            totals[x] = '6'
            for y in poss[5]:
                if len(set(x)-set(y)) == 1:
                    totals[y] = '5'

    final.append(int(''.join([totals.get(k, '3') for k in sorted_display[i]])))

print(sum(final))