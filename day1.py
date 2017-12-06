def day1(num):
    total= 0
    for x in range(len(num)-1):
        if num[x]==num[x+1]:
            total += int(num[x])
    if num[-1] == num[0]:
        total += int(num[-1])
    print total


def day1_2(num):
    jump = len(num)/2
    total = 0
    for x in range(len(num)/2):
        if num[x] == num[x+jump]:
            total += int(num[x]) * 2
    print total
