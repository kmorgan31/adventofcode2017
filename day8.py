def evaluate_condition(register, op, value):
    if op=='<':
        return register < value
    elif op=='<=':
        return register <= value
    elif op=='>':
        return register > value
    elif op=='>=':
        return register >= value
    elif op=='==':
        return register == value
    elif op=='!=':
        return register != value

def evaluate_inc_dec(register, op, value):
    if op == 'inc':
        return register + value
    elif op == 'dec':
        return register - value
    

def day8(filename):
    registers = dict()
    highest_value = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.split()
            if evaluate_condition(registers.get(line[4], 0), line[5], int(line[6])):
                registers[line[0]] = evaluate_inc_dec(registers.get(line[0], 0), line[1], int(line[2]))

            if len(registers) > 0:
                curr_highest = max(registers.values())
                if curr_highest > highest_value:
                    highest_value = curr_highest

    print highest_value
    print max(registers.values())
    print max(registers, key=registers.get)
            
            
