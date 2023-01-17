from collections import defaultdict
import heapq

def shortest_route(distance_dict):
    route_heap = []
    for (source,destinations) in distance_dict.items():
        for destination in destinations:
            heapq.heappush(route_heap,(destination[1],destination[0],[source,destination[0]]))

    while route_heap:
        route = heapq.heappop(route_heap)
        source = route[1]
        visited = route[2]
        if len(visited) == len(distance_dict):
            min_cost = route[0]
            break
        for destination in distance_dict[source]:
            if destination[0] not in visited:
                cost = route[0] + destination[1]
                new_visited = visited + [destination[0]]
                heapq.heappush(route_heap,(cost,destination[0],new_visited))
    return min_cost

def longest_route(distance_dict):
    route_heap = []
    for (source,destinations) in distance_dict.items():
        for destination in destinations:
            heapq.heappush(route_heap,(destination[1],destination[0],[source,destination[0]]))

    max_cost = 0
    while route_heap:
        route = heapq.heappop(route_heap)
        source = route[1]
        visited = route[2]
        if len(visited) == len(distance_dict):
            if route[0] > max_cost:
                max_cost = route[0]
                best_path = visited
        for destination in distance_dict[source]:
            if destination[0] not in visited:
                cost = route[0] + destination[1]
                new_visited = visited + [destination[0]]
                heapq.heappush(route_heap,(cost,destination[0],new_visited))
    return max_cost,best_path  


with open('input.txt') as f:
    lines = f.readlines()

distance_dict = defaultdict(list)
for line in lines:
    split_route = line.split()
    distance_dict[split_route[0]].append((split_route[2],int(split_route[4])))
    distance_dict[split_route[2]].append((split_route[0],int(split_route[4])))

print(shortest_route(distance_dict))
print(longest_route(distance_dict))