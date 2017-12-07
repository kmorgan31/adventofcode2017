def day4(filename):
    part_one_count = 0
    part_two_count = 0

    with open(filename, 'r') as f:
        for line in f:
            words_set = set()
            words = line.replace('\n','').split(' ')

            valid = True
            for x in words:
                if x in words_set:
                    valid = False
                    break
                words_set.add(x)

            if valid:
                part_one_count += 1

    print part_one_count

def day4_2(filename):
    part_two_count = 0

    with open(filename, 'r') as f:
        for line in f:
            words_set = set()
            words = line.replace('\n','').split(' ')

            valid = True
            for x in words:
                lst_x = ''.join(sorted(list(x)))
                if lst_x in words_set:
                    valid = False
                    break
                words_set.add(lst_x)

            if valid:
                part_two_count += 1

    print part_two_count
