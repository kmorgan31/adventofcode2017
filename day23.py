registers = { x: 0 for x in 'bcdefgh'}

def day23(filename=None):
    if not filename:
        filename = 'day23.txt'
    with open(filename, 'r') as f:
        lines = [line.split() for line in f.read().strip().split('\n')]
    
    m = 0
    l = 0
    registers['a'] = 0
    
    def get_value(value):
        if value in registers.keys():
            return registers[value]
        return int(value)

    while  l < len(lines):
        i, x, y = lines[l]
        
        if i == 'jnz':
            if get_value(x) != 0:
                l += get_value(y)
            else:
                l += 1
        else:
            if i == 'set':
                registers[x] = get_value(y)
            elif i== 'sub':
                registers[x] -= get_value(y)
            elif i == 'mul':
                registers[x] *= get_value(y)
                m += 1
            l += 1
    return m

def day23_2(filename=None):
    h = 0
    b = 109900
    c = 126900

    for d in range(b, c+1, 17):
        for e in range(2,d):
            if d % e == 0:
                h += 1
                break
    print h
                
