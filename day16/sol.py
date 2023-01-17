
import re

with open('input.txt') as f:
    lines = f.readlines()

tickertape = {'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}

min_score = 1000
min_score_p2 = 1000
for line in lines:
    details = re.match(r'Sue (\d+): (.+): (\d+), (.+): (\d+), (.+): (\d+)',line.strip())
    aunt_sue_score = abs(int(details.group(3)) - tickertape[details.group(2)]) + abs(int(details.group(5)) - tickertape[details.group(4)] + abs(int(details.group(7)) - tickertape[details.group(6)]))
    if aunt_sue_score < min_score:
        gifting_aunt = details.group(1)
        min_score = aunt_sue_score

    aunt_sue_score_p2 = 0
    for n in [2,4,6]:
        if details.group(n) == 'cats' or details.group(n) == 'trees':
            aunt_sue_score_p2 += abs(min((int(details.group(n+1)) - tickertape[details.group(n)]),0))
        elif details.group(n) == 'pomeranians' or details.group(n) == 'goldfish':
            aunt_sue_score_p2 += abs(max((int(details.group(n+1)) - tickertape[details.group(n)]),0))
        else:
            aunt_sue_score_p2 += abs(int(details.group(n+1))-tickertape[details.group(n)])

    if aunt_sue_score_p2 < min_score_p2:
        gifting_aunt_p2 = details.group(1)
        min_score_p2 = aunt_sue_score_p2


print(gifting_aunt)
print(gifting_aunt_p2)