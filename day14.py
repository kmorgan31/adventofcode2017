from day10 import day10_2

def convert_hex_to_bin(hex_num):
    return bin(int(hex_num, 16))[2:].zfill(128)

def day14(key_string):
    count_ones = 0
    for x in range(128):
        row_input = '{}-{}'.format(key_string, x)
        knot_hash = day10_2(row_input)
        bits = convert_hex_to_bin(knot_hash)
        count_ones += bits.count('1')
    return count_ones

def get_grid(key_string):
    grid = []
    for x in range(128):
        row_input = '{}-{}'.format(key_string, x)
        knot_hash = day10_2(row_input)
        bits = convert_hex_to_bin(knot_hash)
        grid += [list(bits)]
    return grid

def day14_2(key_string):
    regions = {}
    explored = set()
    found = set()
    
    grid = get_grid(key_string)
    
    def explore(x,y):
        if x>=0 and x<128 and y>=0 and y<128 and (x,y) not in found:
            if grid[x][y] == '1':
                # add curr pos to explored and found
                explored.add((x,y))
                found.add((x,y))

                # explore adjacent
                return [(x,y)] + explore(x+1,y) + explore(x-1,y) + explore(x,y+1) + explore(x,y-1)
        return []

    region_count = 0
    for x in range(128):
        for y in range(128):
            if (x,y) not in explored and grid[x][y]=='1':
                # new region found
                region_count += 1
                found = set()
                regions[region_count] = explore(x,y)
    print region_count

