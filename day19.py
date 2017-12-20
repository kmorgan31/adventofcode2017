def day19(diagram=None):
    if(diagram):
        diagram = [list(line) for line in diagram.split('\n')]
    else: 
        with open('day19.txt', 'r') as f:
            diagram = [list(line) for line in f.readlines()]

    letters = []
    # starting position
    x = diagram[0].index('|')
    y = 0

    direction = 'D' #down
    curr_value = "|"
    steps = 0

    while curr_value != ' ':
        steps += 1

        if direction == 'D':
            y += 1
        elif direction == 'U':
            y -= 1
        elif direction == 'L':
            x -= 1
        elif direction == 'R':
            x += 1

        curr_value = diagram[y][x]

        # change direction
        if curr_value == '+':
            if direction in ('D', 'U'):
                if diagram[y][x-1] != ' ':
                    direction = 'L'
                else:
                    direction = 'R'
            else:
                if diagram[y-1][x] != ' ':
                    direction = 'U'
                else:
                    direction = 'D'
                    
        # add letter
        elif curr_value not in ('|', '-'):
             letters.append(curr_value)
    print steps
    print ''.join(letters)
        
