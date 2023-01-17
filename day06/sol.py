with open('input.txt') as f:
    lines = f.readlines()

instructions = [x.split() for x in lines]

grid_p1 = {(x,y) : 0 for x in range(1000) for y in range(1000)}
grid_p2 = {(x,y) : 0 for x in range(1000) for y in range(1000)}
for instruction in instructions:
    if instruction[0] == 'turn':
        left_top = [int(x) for x in instruction[2].split(',')]
        right_bottom = [int(x) for x in instruction[4].split(',')]
        if instruction[1] == 'on':
            grid_p1 = {k : 1 if k[0] >= left_top[0] and k[0] <= right_bottom[0] and k[1] >= left_top[1] and k[1] <= right_bottom[1] else v for (k,v) in grid_p1.items()}
        else:
            grid_p1 = {k : 0 if k[0] >= left_top[0] and k[0] <= right_bottom[0] and k[1] >= left_top[1] and k[1] <= right_bottom[1] else v for (k,v) in grid_p1.items()}
    else:
        left_top = [int(x) for x in instruction[1].split(',')]
        right_bottom = [int(x) for x in instruction[3].split(',')]
        grid_p1 = {k : 1-v if k[0] >= left_top[0] and k[0] <= right_bottom[0] and k[1] >= left_top[1] and k[1] <= right_bottom[1] else v for (k,v) in grid_p1.items()}

    if instruction[0] == 'turn':
        left_top = [int(x) for x in instruction[2].split(',')]
        right_bottom = [int(x) for x in instruction[4].split(',')]
        if instruction[1] == 'on':
            grid_p2 = {k : v+1 if k[0] >= left_top[0] and k[0] <= right_bottom[0] and k[1] >= left_top[1] and k[1] <= right_bottom[1] else v for (k,v) in grid_p2.items()}
        else:
            grid_p2 = {k : max(v-1,0) if k[0] >= left_top[0] and k[0] <= right_bottom[0] and k[1] >= left_top[1] and k[1] <= right_bottom[1] else v for (k,v) in grid_p2.items()}
    else:
        left_top = [int(x) for x in instruction[1].split(',')]
        right_bottom = [int(x) for x in instruction[3].split(',')]
        grid_p2 = {k : v+2 if k[0] >= left_top[0] and k[0] <= right_bottom[0] and k[1] >= left_top[1] and k[1] <= right_bottom[1] else v for (k,v) in grid_p2.items()}

print(sum(grid_p1.values()))
print(sum(grid_p2.values()))
