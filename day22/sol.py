from collections import deque
from copy import deepcopy

boss_hp = 55
boss_damage = 8
player_hp = 50
player_mana = 500

spells = [[53,0,4,0,0,0],
            [73,0,2,2,0,0],
            [113,6,0,0,7,0],
            [173,6,3,0,0,0],
            [229,5,0,0,0,101]]

def wizard_simulator(hp_loss):
    strategies = deque()
    strategies.append([0,0,player_hp,boss_hp,player_mana,0,0,0,0,0])

    while strategies:
        spent_mana = 0
        strategy = strategies.popleft()
        if strategy[0] == 0:
            if strategy[-1] >= 1:
                strategy[4] += spells[4][-1]
            if strategy[-2] >= 1:
                strategy[3] -= spells[3][2]

            strategy[2] -= hp_loss

            if strategy[2] <= 0:
                continue

            for n in range(5):
                strategy[5+n] = max(0,strategy[5+n] - 1)

            for n in range(5):
                new_strategy = deepcopy(strategy)
                new_strategy[0] = 1
                if new_strategy[5+n] == 0:
                    new_strategy[1] += spells[n][0]
                    new_strategy[2] += spells[n][-3]
                    new_strategy[3] -= spells[n][2] if spells[n][1] == 0 else 0
                    new_strategy[4] -= spells[n][0]
                    new_strategy[5+n] = spells[n][1]
                if new_strategy[2] > 0 and new_strategy[3] > 0 and new_strategy[4] >= 0:
                    strategies.append(new_strategy)
                elif new_strategy[3] <= 0:
                    spent_mana = new_strategy[1]
        else:
            new_strategy = deepcopy(strategy)
            new_strategy[0] = 0
            if new_strategy[-1] >= 1:
                new_strategy[4] += spells[4][-1]
            if new_strategy[-2] >= 1:
                new_strategy[3] -= spells[3][2]

            if new_strategy[-3] > 1:
                new_strategy[2] = new_strategy[2] + spells[2][-2] - boss_damage
            else:
                new_strategy[2] -= boss_damage

            for n in range(5):
                new_strategy[5+n] = max(0,new_strategy[5+n] - 1)
            
            if new_strategy[2] > 0 and new_strategy[3] > 0 and new_strategy[4] >= 0:
                strategies.append(new_strategy)
            elif new_strategy[3] <= 0:
                spent_mana = new_strategy[1]
        
        if spent_mana:
            return spent_mana


print(wizard_simulator(0))
print(wizard_simulator(1))        
            
