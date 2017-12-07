import math

def day_3(num):
    side = math.ceil(math.sqrt(num))+1

    brc = side**2
    blc = brc - (side - 1)
    tlc = blc - (side - 1)
    trc = tlc - (side - 1)
    mid = math.ceil((tlc + trc)/2)
    l1 = num - mid
    l2 = math.ceil((side - 1)/2)
    print l1+l2
