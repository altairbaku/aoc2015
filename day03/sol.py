with open('input.txt') as f:
    lines = f.readlines()

step = {'^':[1,0],'v':[-1,0],'>':[0,1],'<':[0,-1]}

pos = [0,0]
santa_pos = [0,0]
robo_santa_pos = [0,0]

visits_p1 = set()
visits_p2 = set()
for line in lines:
    moves = [x for x in line.strip()]
    for move in moves:
        pos = tuple([y+z for y,z in zip(pos,step[move])])
        visits_p1.add(pos)
    for n in range(len(moves)):
        if n%2 == 0:
            santa_pos = tuple([y+z for y,z in zip(santa_pos,step[moves[n]])])
            visits_p2.add(santa_pos)
        else:
            robo_santa_pos = tuple([y+z for y,z in zip(robo_santa_pos,step[moves[n]])])
            visits_p2.add(robo_santa_pos)

print(len(visits_p1))
print(len(visits_p2))