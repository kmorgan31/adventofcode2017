lst = 'abcdefghijklmnop'
with open('day16.txt', 'r') as f:
    moves = f.read().strip().split(',')

def spin(lst, x):
    return lst[-x:] + lst[:-x]

def exchange(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return lst

def partner(lst, A, B):
    a, b = lst.index(A), lst.index(B)
    return exchange(lst, a, b)

def perform_dance(lst, contents):
    for move in contents:
        x = move[0]
        y = move[1:].split('/')
    
        if x == 's':
            lst = spin(lst, int(y[0]))
        elif x == 'x':
            lst = exchange(lst, int(y[0]), int(y[1]))
        elif x == 'p':
            lst = partner(lst, y[0], y[1])
    return ''.join(lst)

def day16(cycles, lst):
    seen = []
    for i in xrange(cycles):
        if lst in seen:
            print seen[cycles % i]
            return
        seen.append(lst)

        lst = perform_dance(list(lst), moves)
    return lst

print "Part one: ", day16(1, lst[:])
print "Part two: ", day16(1000000000, lst[:]) 
