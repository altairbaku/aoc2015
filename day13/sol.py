import heapq

def optimal_seating(happy_dict,people_set):
    seating_options = []
    start_person = 'Alice'
    for person in people_set:
        if person != start_person:
            heapq.heappush(seating_options,(happy_dict[(start_person,person)] + happy_dict[(person,start_person)],[start_person,person]))

    min_cost = 0
    while seating_options:
        seating_scheme = heapq.heappop(seating_options)
        seated_people = seating_scheme[1]
        cost = seating_scheme[0]
        for person in people_set:
            if person not in seated_people:
                if len(seated_people) < (len(people_set) - 1):
                    new_cost = cost + happy_dict[(seated_people[-1],person)] + happy_dict[(person,seated_people[-1])]
                    heapq.heappush(seating_options,(new_cost,seated_people + [person]))
                else:
                    new_cost = cost + happy_dict[(seated_people[-1],person)] + happy_dict[(person,seated_people[-1])] + happy_dict[(person,seated_people[0])] + happy_dict[(seated_people[0],person)]
                    min_cost = min(min_cost,new_cost)
                    break

    max_happiness = -min_cost        
    return max_happiness


with open('input.txt') as f:
    lines = f.readlines()

happy_dict = dict()
people_set = set()
for line in lines:
    happiness_info = line.strip().split()
    personA = happiness_info[0]
    personB = happiness_info[-1][:-1]
    happiness = happiness_info[3]
    people_set.add(personA)
    if happiness_info[2] == 'gain':
        happy_dict[(personA,personB)] = -int(happiness)
    else:
        happy_dict[(personA,personB)] = int(happiness)

print(optimal_seating(happy_dict,people_set))

myself = 'Manav'
people_set.add(myself)
for person in people_set:
    if person != 'myself':
        happy_dict[(myself,person)] = 0
        happy_dict[(person,myself)] = 0

print(optimal_seating(happy_dict,people_set))