import utils.fileutils as futils

inp = futils.read_list("../data/day9.txt")
target = 69316178
start_idx, end_idx = 0, 0
res = 0
while end_idx < len(inp):
    if res == target and end_idx != start_idx:
        min_val, max_val = 69316178, 0
        for _num in inp[start_idx:end_idx + 1]:
            num = int(_num)
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num
        print("min_val: {0} || max_val: {1}".format(min_val, max_val))
        print("Result: {0}".format(min_val + max_val))
        break
    if res >= target:
        res -= int(inp[start_idx])
        start_idx += 1
    elif res < target:
        res += int(inp[end_idx])
        end_idx += 1
