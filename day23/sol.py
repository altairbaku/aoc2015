def run_program(registers,instructions):
    i = 0
    while True:
        if i >= len(instructions):
            break
        instruction = instructions[i].split()
        if instruction[0] == 'inc':
            registers[instruction[1][0]] += 1
        elif instruction[0] == 'hlf':
            registers[instruction[1][0]] /= 2
        elif instruction[0] == 'tpl':
            registers[instruction[1][0]] *= 3
        elif instruction[0] == 'jmp':
            i += (int(instruction[1]) - 1)
        elif instruction[0] == 'jie' and registers[instruction[1][0]] % 2 == 0:
            i += (int(instruction[2]) - 1)
        elif instruction[0] == 'jio' and registers[instruction[1][0]] == 1:
            i += (int(instruction[2]) - 1)
        i += 1
    return(registers['b'])


with open('input.txt') as f:
    instructions = f.readlines()

print(run_program({'a' : 0, 'b' : 0},instructions))
print(run_program({'a' : 1, 'b' : 0},instructions))


    
    