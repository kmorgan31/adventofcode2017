def day11(filename):
    with open(filename, 'r') as f:
        contents = f.read().split(',')

    steps = []
    directions = ['n', 'ne', 'se', 's', 'sw', 'nw']
    furthest = 0

    for x in contents:
        # set relative positions of directions, similar to a triangle
        # angles - A, B, C
        # opposite sides - a, b, c
        A_pos = directions.index(x)
        B_pos = (A_pos + 2) % len(directions)
        C_pos = (B_pos + 2) % len(directions)
        
        a_pos = (A_pos + 3) % len(directions)
        b_pos = (B_pos + 3) % len(directions)
        c_pos = (C_pos + 3) % len(directions)

        # current direction = directions[A_pos]
        if directions[a_pos] in steps:
            # opposite - they cancel
            steps.remove(directions[a_pos])
        elif directions[B_pos] in steps:
            # become the directions between them
            steps.remove(directions[B_pos])
            steps.append(directions[c_pos])
        elif directions[C_pos] in steps:
            # become the directions between them
            steps.remove(directions[C_pos])
            steps.append(directions[b_pos])
        else:
            # add current direction to steps
            steps.append(directions[A_pos])
            
        # part two    
        if len(steps) > furthest:
            furthest = len(steps)
    
    print len(steps)
    print furthest
