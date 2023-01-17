with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    directions = [1 if char == '(' else -1 for char in line.strip()]

p1 = sum(directions)
print(p1)

floor = 0
for i in range(len(directions)):
    floor += directions[i]
    if floor == -1:
        p2 = i+1
        break
print(p2)
