def day10(puzzle_input=None):
    if not puzzle_input:
        puzzle_input = [165, 1, 255, 31, 87, 52, 24, 113,
                        0, 91, 148, 254, 158, 2, 73, 153]

    lst = range(256)
    curr_pos = 0
    skip_size = 0

    for x in puzzle_input:

        end_idx = curr_pos + x - 1

        for y in range(x/2):
            temp = lst[(curr_pos + y) % len(lst)]
            lst[(curr_pos + y) % len(lst)] = lst[(end_idx - y) % len(lst)]
            lst[(end_idx - y) % len(lst)] = temp

        # increments
        curr_pos += (x + skip_size) % len(lst)
        skip_size += 1

    print lst[0] * lst[1]


# alternative to day10 part 1 soln
def day10_1(puzzle_input=None):
    if not puzzle_input:
        puzzle_input = [165, 1, 255, 31, 87, 52, 24, 113,
                        0, 91, 148, 254, 158, 2, 73, 153]

    lst = range(256)
    curr_pos = 0
    skip_size = 0

    for x in puzzle_input:
        # get length
        length = []
        for y in range(x):
            pos = (y + curr_pos) % len(lst)
            length += [lst[pos]]

        reversed_length = length[::-1]

        # put it back into lst
        for y in range(x):
            pos = (y + curr_pos) % len(lst)
            lst[pos] = reversed_length[y]

        # increments
        curr_pos += (x + skip_size) % len(lst)
        skip_size += 1

    return lst[0] * lst[1]


def calc_xor_value(lst):
    ans = 0
    for x in lst:
        ans ^= x
    return ans


def day10_2(puzzle_input=None):
    if not puzzle_input:
        puzzle_input = '165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153'

    lst = range(256)
    curr_pos = 0
    skip_size = 0

    # prepare puzzle_input
    puzzle_input = map(ord, puzzle_input) + [17, 31, 73, 47, 23]

    # part 1 looped 64 times
    for i in range(64):
        for x in puzzle_input:
            end_idx = curr_pos + x - 1

            for y in range(x/2):
                temp = lst[(curr_pos + y) % len(lst)]
                lst[(curr_pos + y) % len(lst)] = lst[(end_idx - y) % len(lst)]
                lst[(end_idx - y) % len(lst)] = temp

            # increments
            curr_pos += (x + skip_size) % len(lst)
            skip_size += 1

    # get dense hash
    ans_lst = []
    for i in range(0, len(lst), 16):
        chunk = lst[i:i+16]
        ans_lst.append(calc_xor_value(chunk))

    # convert to hex string
    ans_lst = ['{:02x}'.format(x) for x in ans_lst]
    return ''.join(ans_lst)
