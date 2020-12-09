import utils.fileutils as futils

inp = futils.read_list("../data/day8.txt")
instruction_ids_set = set()
line_count = 0
accumulator = 0

while line_count < len(inp):
    instruction_ids_set.add(line_count)
    line_splits = inp[line_count].split()
    instr, val = line_splits[0], int(line_splits[1])
    if instr == "acc":
        accumulator += val
        line_count += 1
    elif instr == "jmp":
        line_count += val
    elif instr == "nop":
        line_count += 1
    else:
        print("IMPOSSIBLE")
    if line_count in instruction_ids_set:
        print("acc = {0}".format(accumulator))
        break
