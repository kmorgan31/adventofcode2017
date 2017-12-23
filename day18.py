from collections import defaultdict

filename = 'day18.txt'
with open(filename, 'r') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]

def day18():
    last = 0
    line_no = 0
    registers = {}
    
    def get_value(value):
        if value in "qwertyuiopasdfghjklzxcvbnm":
            return registers[value]
        return int(value)

    while line_no < lines:
        line = lines[line_no]
        instruction = line[0]
        register = line[1]

        # initiate register
        if not (register in registers.keys()):
            registers[register] = 0

        if instruction == 'set':
            registers[register] = get_value(line[2])
        elif instruction == 'add':
            registers[register] += get_value(line[2])
        elif instruction == 'mul':
            registers[register] *= get_value(line[2])
        elif instruction == 'mod':
            registers[register] %= get_value(line[2])
        elif instruction == 'snd':
            last = registers[register]
        elif instruction == 'rcv':
            if registers[register] != 0:
                break
        elif instruction == 'jgz':
            if registers[register] > 0:
                line_no += int(line[2])
                continue
        line_no+=1
    print last

def day18_2():
    def get_value(value):
        if value in "qwertyuiopasdfghjklzxcvbnm":
            return curr_registers[value]
        return int(value)
    
    p0 = defaultdict(int)
    p1 = defaultdict(int)
    p1['p'] = 1
    programs = [p0, p1]

    send_count = 0

    line_nos = [0,0]
    queues = [[],[]]
    state = ["ok", "ok"]

    pr = 0 # current program
    curr_registers = programs[pr]
    curr_idx = line_nos[0]

    while True:
        line = lines[curr_idx]
        instruction = line[0]

        if not (line[1] in curr_registers.keys()):
            curr_registers[line[1]] = 0

        if instruction == 'snd':
            if pr == 1: # p1 send count
                send_count += 1
            queues[pr].append(get_value(line[1]))
        elif instruction == 'set':
            curr_registers[line[1]] = get_value(line[2])
        elif instruction == 'add':
            curr_registers[line[1]] += get_value(line[2])
        elif instruction == 'mul':
            curr_registers[line[1]] *= get_value(line[2])
        elif instruction == 'mod':
            curr_registers[line[1]] %= get_value(line[2])
        elif instruction == 'rcv':
            if queues[1-pr]:
                state[pr] = "ok"
                curr_registers[line[1]] = queues[1-pr].pop(0)
            else:
                if state[1-pr] == "done":
                    break #deadlocked
                if len(queues[pr])==0 and state[1-pr]=="r":
                    break #other waiting to receive
                line_nos[pr] = curr_idx
                state[pr] = "r" # wait to receive
                pr = 1-pr # switch programs
                curr_idx = line_nos[pr]-1
                curr_registers = programs[pr]
        elif instruction == 'jgz':
            if get_value(line[1]) > 0:
                curr_idx += get_value(line[2])-1
        curr_idx += 1

        if not 0<=curr_idx<len(lines):
            if state[1-pr] == "done":
                break # both done
            state[pr] = "done"
            line_nos[pr] = curr_idx
            pr = 1-pr
            curr_idx = line_nos[pr]
            curr_registers = programs[pr]
    print send_count
