from copy import deepcopy

def get_neighbors(grid_pos):
    neighbors = {(grid_pos[0] + x,grid_pos[1]+y) for x in [-1,0,1] for y in [-1,0,1]}
    neighbors.remove(grid_pos)
    return neighbors

with open('input.txt') as f:
    lines = f.readlines()

on_original = set()
off_original = set()

for i in range(len(lines)):
    for j in range(len(lines[0])-1):
        if lines[i][j] == '#':
            on_original.add((i,j))
        elif lines[i][j] == '.':
            off_original.add((i,j))


on = deepcopy(on_original)
off = deepcopy(off_original)
all_lights = set()
all_lights.update(on)
all_lights.update(off)

for n in range(100):
    new_on = set()
    new_off = set()
    for light in all_lights:
        on_neighbors = sum([1 if neighbor in on else 0 for neighbor in get_neighbors(light)])
        if (light in on and on_neighbors in [2,3]) or (light in off and on_neighbors == 3):
            new_on.add(light)
        else:
            new_off.add(light)
    on = new_on
    off = new_off

print(len(on))

corners = {(0,99),(0,0),(99,0),(99,99)}
for corner in corners:
    all_lights.remove(corner)
    if corner in off_original:
        off_original.remove(corner)
    on_original.add(corner)

on = deepcopy(on_original)
off = deepcopy(off_original)
for n in range(100):
    new_on = {(0,99),(0,0),(99,0),(99,99)}
    new_off = set()
    for light in all_lights:
        on_neighbors = sum([1 if neighbor in on else 0 for neighbor in get_neighbors(light)])
        if (light in on and on_neighbors in [2,3]) or (light in off and on_neighbors == 3):
            new_on.add(light)
        else:
            new_off.add(light)
    on = new_on
    off = new_off

print(len(on))