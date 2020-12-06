import utils.fileutils as futils

inp = futils.read_list("../data/day6.txt")
nums_set = set()
res_count = 0
for line in inp:
    if line == "":
        res_count += len(nums_set)
        nums_set = set()
        continue
    for ch in line:
        nums_set.add(ch)

res_count += len(nums_set)
print("Sum of counts: {0}".format(res_count))
