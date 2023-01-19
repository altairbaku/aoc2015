from itertools import combinations

def optimal_group(packages,group_size):
    package_sum = sum(packages)/group_size
    smallest_group_size = 2
    combos = set()
    while True:
        combos = [seq for seq in combinations(packages, smallest_group_size)
          if sum(seq) == package_sum]
        if combos:
            break
        smallest_group_size += 1
    best = 100000000000
    for combo in combos:
        result = 1
        for x in combo:
            result = result * x
        if result < best:
            best= result
    return best

with open('input.txt') as f:
    package_list = f.readlines()

packages = set()
for package in package_list:
    packages.add(int(package))


print(optimal_group(packages,3))
print(optimal_group(packages,4))