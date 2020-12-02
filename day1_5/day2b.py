import utils.fileutils as futils

inp = futils.read_list("../data/day2.txt")
valid_count = 0
for line in inp:
    pwd_range, ch, pwd = line.split()
    pwd_len = len(pwd)
    idx1, idx2 = int(pwd_range.split("-")[0]) - 1, int(pwd_range.split("-")[1]) - 1
    ch = ch[0]
    seen_flag = False
    if pwd_len > idx1 >= 0 and pwd[idx1] == ch:
        valid_count += 1
        seen_flag = True
    if 0 <= idx2 < pwd_len and pwd[idx2] == ch:
        if seen_flag:
            valid_count -= 1
        else:
            valid_count += 1
print("Valid count: {0}".format(valid_count))
