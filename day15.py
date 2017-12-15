def generator(x, f, m=1):
    while True:
        x = x * f % 2147483647
        if x%m == 0:
            yield x 

def day15(A_start, B_start, n, A_multiple=1, B_multiple=1):
    genA = generator(A_start, 16807, A_multiple)
    genB = generator(B_start, 48271, B_multiple)

    matches=0
    for x in xrange(n):
        a = genA.next()
        b = genB.next()
        if a & 0xFFFF == b & 0xFFFF:
            matches += 1
    return matches
