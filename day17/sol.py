import itertools

with open('input.txt') as f:
    lines = f.readlines()

containers = []
for line in lines:
    containers.append(int(line.strip()))

eggnog = 150

container_combos = [seq for n in range(len(containers),2,-1) for seq in itertools.combinations(containers,n) if sum(seq) == eggnog]
print(len(container_combos))

combo_lens = [len(x) for x in container_combos]
print(sum([1 if y == min(combo_lens) else 0 for y in combo_lens]))