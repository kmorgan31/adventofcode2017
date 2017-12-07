def day2(filename):
    part_one_total = 0
    part_two_total = 0

    with open(filename, 'r') as f:
        for line in f:
            nums = map(int,line.split('\t'))
            part_one_total = max(nums) - min(nums)

            for x in range(len(nums)):
                for y in range(len(nums)):
                    if x != y:
                        if nums[x] % nums[y] == 0:
                            part_two_total += int(nums[x]/nums[y])
    print part_one_total
    print part_two_total
