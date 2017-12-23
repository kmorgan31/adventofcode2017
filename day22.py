grid_map = {
    '.': 'l',
    'W': 'w',
    '#': 'r',
    'F': 'f'
}

ds = ['n', 'e', 's', 'w']
def get_direction(d, turn):
    i = ds.index(d)
    if turn == 'r':
        return ds[(i+1)%len(ds)]
    elif turn == 'l':
        return ds[(i-1)%len(ds)]
    elif turn == 'w':
        return d
    else:
        return ds[(i+2)%len(ds)]

ns = ['.', 'W', '#', 'F']
def get_new_state(s):
    i = ns.index(s)
    return ns[(i+1)%len(ns)]

def move(x,y, d):
    if d=='n':
        x -= 1
    elif d=='s':
        x += 1
    elif d=='e':
        y += 1
    elif d=='w':
        y -= 1
    return x,y

def add_buffer(grid, extra):
    new_len = len(grid) + (2*extra)
    clean_row = ['.'] * new_len
    extra_col = ['.'] * extra
    new_grid = []
    for x in xrange(extra):
        new_grid += [clean_row[:]]
    for x in grid:
        new_grid += [extra_col[:] + x + extra_col[:]]
    for x in xrange(extra):
        new_grid += [clean_row[:]]
    return new_grid

def print_grid(grid, i, j):
    for x in range(len(grid)):
        row = ''
        for y in range(len(grid[x])):
            if x==i and y==j:
                row += '[' + grid[x][y] + ']'
            else:
                row += ' ' + grid[x][y] + ' '
        print row
    print '\n'

def day22(filename=None, extra=3):
    if not filename:
        filename = 'day22.txt'

    with open(filename, 'r') as f:
        grid = [list(line) for line in f.read().strip().split('\n')]

    grid = add_buffer(grid, 200)

    got_infected = 0
    direction = 'n'
    x = y = len(grid)/2

    for i in xrange(10000):
        direction = get_direction(direction, grid_map[grid[x][y]])
        
        if grid[x][y] == '.':
            got_infected += 1
            grid[x][y] = '#'
        else:
            grid[x][y] = '.'

        # move
        x,y = move(x,y, direction)

    # get number infected
    return got_infected

def day22_2(filename=None, extra=250):
    if not filename:
        filename = 'day22.txt'

    with open(filename, 'r') as f:
        grid = [list(line) for line in f.read().strip().split('\n')]

    grid = add_buffer(grid, extra)

    got_infected = 0
    direction = 'n'
    x = y = len(grid)/2

    for i in xrange(10000000):
        direction = get_direction(direction, grid_map[grid[x][y]])
        
        grid[x][y] = get_new_state(grid[x][y])
        if grid[x][y] == '#':
            got_infected += 1

        # move
        x,y = move(x,y, direction)

    # get number infected
    return got_infected
    
