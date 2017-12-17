def day17(step, num_values=2018):
    buffer_lst = [0]
    curr_pos = 0
    for x in xrange(1, num_values):
        curr_pos = ((curr_pos + step) % x) + 1
        buffer_lst.insert(curr_pos, x)
    print buffer_lst[(curr_pos+1)%num_values]

def day17_2(step, at_index=1):
    curr_pos = 0
    for x in xrange(50000000):
        curr_pos = ((curr_pos + step) % (x+1)) + 1
        if curr_pos == at_index:
            out = x+1 #value that would be inserted
    print out
