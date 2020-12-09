import utils.fileutils as futils

inp = futils.read_list("../data/day8.txt")
len_inp = len(inp)
# instruction_ids_set = set()

for line_change in range(len_inp):
    new_inp = list(inp)
    if new_inp[line_change].split()[0] == 'jmp':
        new_inp[line_change] = 'nop ' + new_inp[line_change].split()[1]
    elif new_inp[line_change].split()[0] == 'nop':
        new_inp[line_change] = 'jmp ' + new_inp[line_change].split()[1]
    else:
        continue
    iteration_counter = 0
    line_count = 0
    accumulator = 0
    while 0 <= line_count < len_inp and iteration_counter < len_inp + 1:
        # instruction_ids_set.add(line_count)
        line_splits = new_inp[line_count].split()
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
        iteration_counter += 1
        # if line_count in instruction_ids_set:
        #     print("acc = {0}".format(accumulator))
        #     break
    if line_count == len_inp:
        print(accumulator)
