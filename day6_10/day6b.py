import utils.fileutils as futils

inp = futils.read_list("../data/day6.txt")
nums_dict = dict()
group_size, res_count = 0, 0
for line in inp:
    if line == "":
        # res_count += len(nums_set)
        for k, v in nums_dict.items():
            if v == group_size:
                res_count += 1
        nums_dict = dict()
        group_size = 0
        continue
    group_size += 1
    for ch in line:
        nums_dict[ch] = 1 + nums_dict.get(ch, 0)

for k, v in nums_dict.items():
    if v == group_size:
        res_count += 1
print("Sum of counts: {0}".format(res_count))
