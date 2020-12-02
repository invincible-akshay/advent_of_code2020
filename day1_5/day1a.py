import utils.fileutils as futils

inp = futils.read_list("../data/day1.txt", True)
nums_set = set()
for num in inp:
    if 2020 - num in nums_set:
        print(num*(2020-num))
        break
    nums_set.add(num)
