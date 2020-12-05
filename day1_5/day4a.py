import utils.fileutils as futils

inp = futils.read_list("../data/day4.txt")
row_count = 0
REQUIRED_SET = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
tmp_set = set()
res_count = 0
while row_count < len(inp):
    line = inp[row_count]
    if line == "":
        diff_set = REQUIRED_SET - tmp_set
        if len(diff_set) == 0:
            res_count += 1
        tmp_set = set()
    else:
        for kv in line.split():
            tmp_set.add(kv.split(":")[0])

    row_count += 1

diff_set = REQUIRED_SET - tmp_set
if len(diff_set) == 0:
    res_count += 1

print("{0} valid passports".format(res_count))
