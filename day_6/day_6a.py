import collections

with open('day_6\input.txt') as f:
    init_dict = collections.Counter((map(int,f.readline().split(','))))

def update_timers(start_day):
    fish = {}
    for x in [1,2,3,4,5,6,8]:
        fish[x-1] = start_day[x]
    fish[8]= start_day[0]
    fish[6] = start_day[7] + start_day[0]
    return fish

def count_fish(fish_dict, days):
    for _ in range(0, days):
        fish_dict = update_timers(fish_dict)
    return(sum(fish_dict.values()))

print(count_fish(init_dict, 256))