import utils.fileutils as futils

inp = futils.read_list("../data/day1.txt", True)

inp.sort()
br_flag = False
for i in range(len(inp)-2):
    new_t = 2020 - inp[i]
    start, end = i + 1, len(inp) - 1
    if inp[i] + inp[start] >= 2020:
        continue
    while start < end:
        if inp[start] + inp[end] > new_t:
            end -= 1
        elif inp[start] + inp[end] < new_t:
            start += 1
        else:
            print(inp[i], inp[start], inp[end], inp[i]*inp[start]*inp[end])
            br_flag = True
            break
    if br_flag:
        break
