import utils.fileutils as futils

inp = futils.read_list("../data/day2.txt")
total_count = len(inp)
invalid_count = 0
for line in inp:
    pwd_range, ch, pwd = line.split()
    start, end = int(pwd_range.split("-")[0]), int(pwd_range.split("-")[1])
    ch = ch[0]
    count = 0
    for c in pwd:
        if c == ch:
            count += 1
        if count > end:
            invalid_count += 1
            break
    if count < start:
        invalid_count += 1
print("Valid count: {0}".format(total_count - invalid_count))
