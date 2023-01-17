with open('input.txt') as f:
    lines = f.readlines()

wrapping_paper = 0
ribbon = 0
for line in lines:
    box = [int(y) for y in line.strip().split('x')]
    areas = [box[x] * box[y] for x in range(3) for y in range(x+1,3)]
    wrapping_paper += (2 * sum(areas) + min(areas))

    perimeter = [box[x] + box[y] for x in range(3) for y in range(x+1,3)]
    ribbon += (2 * min(perimeter)) + (box[0] * box[1] * box[2])

print(wrapping_paper)
print(ribbon)
