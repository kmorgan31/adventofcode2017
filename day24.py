filename = 'day24.txt'    
with open(filename, 'r') as f:
    components = [list(map(int, line.split('/'))) for line in f.read().splitlines()]

def get_score(bridge):
    return sum([sum(component) for component in bridge])

def get_length(bridge):
    return len(bridge)

def get_bridge(bridge, end_port, components):
    available = [component for component in components
                            if end_port in component]
    if not available:
        return [bridge] # dead-end

    bridges = []
    for component in available:
        remaining = components[:]
        remaining.remove(component)
        ports = component[:]
        ports.remove(end_port)
        bridges += get_bridge(bridge + [component], ports[0], remaining)
    return bridges
        
bridges = get_bridge([], 0, components)

part_one_strongest = 0
part_two_strongest = 0
part_two_longest = 0
for b in bridges:
    l = get_length(b)
    s = get_score(b)
    
    if s > part_one_strongest:
        part_one_strongest = s

    if l > part_two_longest:
        part_two_longest = l
        part_two_strongest = s
    elif l == part_two_longest:
        if s > part_two_strongest:
            part_two_strongest = s
            
print part_one_strongest
print part_two_strongest





    
