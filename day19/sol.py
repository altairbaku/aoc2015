from collections import defaultdict
import heapq

def hamming_distance(string1,string2):
    matching = 0
    for xi,yi in zip(string1,string2):
        if xi == yi:
            matching += 1
        else:
            break
    return matching

with open('input.txt') as f:
    lines = f.readlines()

medicine_molecule = lines[-1].strip()
distinct_molecules = set()

replace_dict = defaultdict(list)
for n in range(len(lines) -2):
    replacement = lines[n].strip().split(' => ')
    find = replacement[0]
    replace = replacement[1]
    replace_dict[find].append(replace)
    len_find = len(find)
    for i in range(len(medicine_molecule) - len_find + 1):
        if medicine_molecule[i:i+len_find] == find:
            new_molecule = medicine_molecule[:i] + replace + medicine_molecule[i+len_find:]
            distinct_molecules.add(new_molecule)

print(len(distinct_molecules))

molecule_len = len(medicine_molecule)
queue = []
heapq.heappush(queue,[molecule_len,0,'e'])

distinct_molecules = set()

while queue:
    cur_molecule_details = heapq.heappop(queue)
    cur_molecule = cur_molecule_details[2]
    replace_count = cur_molecule_details[1]
    if cur_molecule == medicine_molecule:
        print(replace_count)
        break
    for find in replace_dict.keys():
        len_find = len(find)
        for i in range(len(cur_molecule) - len_find + 1):
            if cur_molecule[i:i+len_find] == find:
                for replace in replace_dict[find]:
                    new_molecule = cur_molecule[:i] + replace + cur_molecule[i+len_find:]
                    cost = len(new_molecule) - hamming_distance(medicine_molecule[:len(new_molecule)],new_molecule)
                    if new_molecule not in distinct_molecules and len(new_molecule) <= molecule_len:
                        heapq.heappush(queue,[cost,replace_count+1,new_molecule])
                        distinct_molecules.add(new_molecule)

    
