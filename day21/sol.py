import itertools
from math import ceil

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    boss_info = line.strip().split(': ')
    if boss_info[0] == 'Hit Points':
        hit_points_boss = int(boss_info[1])
    elif boss_info[0] == 'Armor':
        armor_boss = int(boss_info[1])
    else:
        damage_boss = int(boss_info[1])

hit_points = 100
weapons = {"Dagger" : [8,4,0],"Shortsword":[10,5,0],"Warhammer":[25,6,0],"Longsword":[40,7,0],"Greataxe":[74,8,0]}
armors = {"Leather" : [13,0,1],"Chanimail":[31,0,2],"Splintmail":[53,0,3],"Bandemail":[75,0,4],"Platemail":[102,0,5]}
rings = {"damage_1":[25,1,0],"damage_2":[50,2,0],"damage_3":[100,3,0],"defense_1":[20,0,1],"defense_2":[40,0,2],"defense_3":[80,0,3]}
combos = [dict(x) for x in itertools.product(weapons.items(),armors.items(),rings.items(),rings.items())]

cheapest_combo = 10000
costliest_combo = 0
for combo in combos:
    zipped_list = zip(*combo.values())
    skill_level = [sum(item) for item in zipped_list]

    if ceil(hit_points_boss/max(1,skill_level[1]-armor_boss)) <= ceil(hit_points/max(1,damage_boss-skill_level[2])):
        cheapest_combo = min(cheapest_combo,skill_level[0])

    if ceil(hit_points_boss/max(1,skill_level[1]-armor_boss)) > ceil(hit_points/max(1,damage_boss-skill_level[2])):
        costliest_combo = max(costliest_combo,skill_level[0])

print(cheapest_combo)
print(costliest_combo)
