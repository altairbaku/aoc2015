import itertools
import re

with open('input.txt') as f:
    lines = f.readlines()

ingredient_properties = []
for line in lines:
    ingredient_properties.append([int(x) for x in re.findall(r'-?\d+',line.strip())])

teaspoons = list(range(0,101))
target = 100
n_ingredients = len(ingredient_properties)
n_properties = len(ingredient_properties[0])
teaspoon_combos = [seq for seq in itertools.permutations(teaspoons,n_ingredients) if sum(seq) == target]

highest_score_p1 = 0
highest_score_p2 = 0
for combo in teaspoon_combos:
    scores = [sum([combo[x]*ingredient_properties[x][y] for x in range(n_ingredients)]) for y in range(n_properties)]
    updated_score = [x if x > 0 else 0 for x in scores]
    result = 1
    for n in range(len(updated_score)-1):
        result = result * updated_score[n]
    highest_score_p1 = max(highest_score_p1,result)
    if highest_score_p2 < result and updated_score[-1] == 500:
        highest_score_p2 = result

print(highest_score_p1)
print(highest_score_p2)
