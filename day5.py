def day5(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        contents = map(int, contents.strip().split())

        steps = 0
        place = 0
        while place < len(contents) and place > -1:
            old = place
            steps += 1
            place += contents[place]
            contents[old] += 1
        print steps

def day5_2(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        contents = map(int, contents.strip().split())

        steps = 0
        place = 0
        while place < len(contents) and place > -1:
            old = place
            steps += 1
            jump = contents[place]
            place += jump
            if jump >= 3:
                contents[old] -= 1
            else:
                contents[old] += 1
        print steps
