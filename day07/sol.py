from copy import deepcopy

with open('input.txt') as f:
    lines = f.readlines()

operators = {'AND':'&','OR':'|','NOT':'~','RSHIFT':'>>','LSHIFT':'<<'}

wire_dict = dict()
for line in lines:
    wire_instruction = line.strip().split(' -> ')
    for word,operator in operators.items():
        wire_instruction[0] = wire_instruction[0].replace(word,operator)
    wire_dict[wire_instruction[1]] = wire_instruction[0]

def solve(wire_dict, wire):
    try:
        wire_dict[wire] = eval(str(wire_dict[wire]))
    except:
        if len(wire_dict[wire]) > 2:
            wires = wire_dict[wire].split()
            if not wires[0].isnumeric() and wires[0] not in list(operators.values()):
                left_wire = solve(wire_dict,wires[0]) 
            elif wires[0].isnumeric():
                left_wire = int(wires[0])
            else:
                left_wire = wires[0]

            if left_wire == '~':
                right_wire = solve(wire_dict,wires[1]) if not wires[1].isnumeric() else int(wires[1])
                wire_dict[wire] = wire_dict[wire].replace(wires[1],str(right_wire % 65536))
            else:
                wire_dict[wire] = wire_dict[wire].replace(wires[0],str(left_wire % 65536))
                right_wire = solve(wire_dict,wires[2]) if not wires[2].isnumeric() else int(wires[2])
                wire_dict[wire] = wire_dict[wire].replace(wires[2],str(right_wire % 65536))
        else:
            value = solve(wire_dict,wire_dict[wire])
            wire_dict[wire] = wire_dict[wire].replace(wire_dict[wire],str(value))
        wire_dict[wire] = eval(str(wire_dict[wire]))
    return wire_dict[wire]

wire_dict_p1 = deepcopy(wire_dict)
p1 = solve(wire_dict_p1,'a')
print(p1)
wire_dict_p2 = deepcopy(wire_dict)
wire_dict_p2['b'] = str(p1)
p2 = solve(wire_dict_p2,'a')
print(p2)
