rules = {}

def day21(filename=None):
    # file of instructions
    if filename is None:
        filename = 'day21.txt'

    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
        for line in lines:
            i, o = line.split(' => ')
            i = tuple([tuple(x) for x in i.split('/')])
            o = tuple([tuple(x) for x in o.split('/')])

            n = len(i)
            def transform(x, y, flip, rev_row, rev_col):
                if rev_row:
                    x = n-1-x
                if rev_col:
                    y = n-1-y
                if flip:
                    x,y = y,x
                return i[x][y]
            
            for flip in (True, False):
                for rev_row in (True, False):
                    for rev_col in (True, False):
                         new_i = tuple([tuple(transform(x,y,flip,rev_row, rev_col) for y in range(n)) for x in range(n)])
                         rules[new_i] = o

    pattern = [list('.#.'), list('..#'), list('###')]

    
    for t in range(19):
        ans = 0
        n = len(pattern)

        for x in range(n):
            for y in range(n):
                if pattern[x][y] == '#':
                    ans += 1
        print t, ans
        
        if n%2==0:
            block = 2
        else:
            block = 3

        new_blocks = []
        for x in range(n/block):
            row = []
            for y in range(n/block):
                i_block = tuple([tuple([pattern[x*block+r][y*block+c] for c in range(block)]) for r in range(block)])
                row.append(rules[i_block])
            new_blocks.append(row)
        new_n = n/block*(block+1)

        def from_block(x,y):
            x0, x1 = x/(block+1), x%(block+1)
            y0, y1 = y/(block+1), y%(block+1)
            return new_blocks[x0][y0][x1][y1]

        new_pattern = [[from_block(x,y) for y in range(new_n)] for x in range(new_n)]
        pattern = new_pattern

    
