with open('day_3\input.txt') as f:
    bits = [line.strip() for line in f]

def rating_calculator(report, criteria):
    totals = [0 for x in range(len(report[0]))]
    for pos in range(len(report[0])):
        if len(report) > 1:
            for x in report:
                if int(x[pos]) == 1:
                    totals[pos] += int(x[pos])
                else:
                    totals[pos] -= 1
            if criteria == 'oxygen':
                if totals[pos] >= 0:
                    report = list(filter(lambda x: int(x[pos]) == 1, report))
                else:
                    report = list(filter(lambda x: int(x[pos]) == 0, report))
            elif criteria == 'CO2':
                if totals[pos] >= 0:
                    report = list(filter(lambda x: int(x[pos]) == 0, report))
                else:
                    report = list(filter(lambda x: int(x[pos]) == 1, report))
    return int(report[0], 2)

oxygen_generator_rating = rating_calculator(bits, 'oxygen')
CO2_scrubber_rating = rating_calculator(bits, 'CO2')

print(oxygen_generator_rating)
print(CO2_scrubber_rating)
print(oxygen_generator_rating * CO2_scrubber_rating)

