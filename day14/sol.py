from math import ceil
with open('input.txt') as f:
    lines = f.readlines()

time = 2503
max_dist = 0
reindeer_tuples = []
for line in lines:
    reindeer_info = line.strip().split()
    speed = int(reindeer_info[3])
    fly_time = int(reindeer_info[6])
    rest_time = int(reindeer_info[13])
    reindeer_tuples.append((speed,fly_time,rest_time))
    time_segments = ceil(time/(fly_time+rest_time))
    distance = time_segments * fly_time * speed
    max_dist = max(max_dist,distance)

reindeer_count = len(reindeer_tuples)
points = [0] * reindeer_count
distances = [0] * reindeer_count
for n in range(time):
    distances = [distances[i]+reindeer_tuples[i][0] if n%(reindeer_tuples[i][1]+reindeer_tuples[i][2]) < reindeer_tuples[i][1] else distances[i] for i in range(reindeer_count)]
    points = [points[j]+1 if distances[j] == max(distances) else points[j] for j in range(reindeer_count)]

print(max(points))