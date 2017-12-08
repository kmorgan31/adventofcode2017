def day6():
    input_list = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
    states = set()
    current_state = ','.join(map(str,input_list))

    num_states = 0
    while current_state not in states:
        num_states += 1
        states.add(current_state)
        val = max(input_list)
        idx = input_list.index(val)
        input_list[idx] = 0
        
        while val != 0:
            idx += 1
            input_list[idx%len(input_list)] += 1
            val -= 1
        current_state = ','.join(map(str,input_list))
    print num_states


def day6_2():
    input_list = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
    states = []
    current_state = ','.join(map(str,input_list))

    num_states = 0
    while current_state not in states:
        num_states += 1
        states += [current_state]
        val = max(input_list)
        idx = input_list.index(val)
        input_list[idx] = 0
        
        while val != 0:
            idx += 1
            input_list[idx%len(input_list)] += 1
            val -= 1
        current_state = ','.join(map(str,input_list))
    print num_states - states.index(current_state)
