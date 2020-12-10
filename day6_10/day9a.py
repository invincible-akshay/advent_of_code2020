import utils.fileutils as futils

inp = futils.read_list("../data/day9.txt")
start_idx, end_idx = 0, 25
num_set = set()
for i in range(start_idx, end_idx):
    num_set.add(int(inp[i]))
while end_idx < len(inp):
    target = int(inp[end_idx])
    break_flag = False
    for i in range(start_idx, end_idx):
        num1 = int(inp[i])
        if num1 != target - num1 and target - num1 in num_set:
            num_set.remove(int(inp[start_idx]))
            start_idx += 1
            end_idx += 1
            num_set.add(target)
            break_flag = True
            break
    if not break_flag:
        print(target)
        break
