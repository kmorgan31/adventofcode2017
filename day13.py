def day13(filename):
    dct = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(': ')
            dct[int(line[0])] = int(line[1])

    def where_caught(num_steps, delay):
        caught = []
        for step in dct.keys():
            time = step + delay
            len_sensor_range = (dct[step]*2)-2
            if time%len_sensor_range == 0:
                caught += [step]
        return caught

    def get_severity(caught):
        severity = 0
        for step in caught:
            severity += (step*dct[step])
        return severity


    num_steps = max(dct.keys())+1

    # part_one
    caught = where_caught(num_steps, 0)
    severity = get_severity(caught)
    print severity

    # part_two
    delay = 0
    while True:
        caught = where_caught(num_steps, delay)
        if caught:
            delay += 1
        else:
            break
    print delay      
                
