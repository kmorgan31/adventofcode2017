tape = [0] # centre of tape

def move_left(pos):
    if pos == 0: # leftmost end of tape
        tape.insert(0, 0)
        # pos stays the same
    else:
        pos -= 1 
    return pos

def move_right(pos):
    if len(tape) == pos+1: # rightmost end of tape
        tape.append(0)
    pos += 1
    return pos

def day25(steps, filename=None):   
    state = 'A'
    pos = 0

    for x in xrange(steps):
        if state == 'A':
            if tape[pos] == 0:
                tape[pos] = 1
                pos = move_right(pos)
                state = 'B'
            else:
                tape[pos] = 0
                pos = move_left(pos)
                state = 'D'
        elif state == 'B':
            if tape[pos] == 0:
                tape[pos] = 1
                pos = move_right(pos)
                state = 'C'
            else:
                tape[pos] = 0
                pos = move_right(pos)
                state = 'F'
        elif state == 'C':
            if tape[pos] == 0:
                tape[pos] = 1
                pos = move_left(pos)
                state = 'C'
            else:
                tape[pos] = 1
                pos = move_left(pos)
                state = 'A'
        elif state == 'D':
            if tape[pos] == 0:
                tape[pos] = 0
                pos = move_left(pos)
                state = 'E'
            else:
                tape[pos] = 1
                pos = move_right(pos)
                state = 'A'
        elif state == 'E':
            if tape[pos] == 0:
                tape[pos] = 1
                pos = move_left(pos)
                state = 'A'
            else:
                tape[pos] = 0
                pos = move_right(pos)
                state = 'B'
        elif state == 'F':
            if tape[pos] == 0:
                tape[pos] = 0
                pos = move_right(pos)
                state = 'C'
            else:
                tape[pos] = 0
                pos = move_right(pos)
                state = 'E'

    return tape.count(1)
        
