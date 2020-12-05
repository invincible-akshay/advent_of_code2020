import utils.fileutils as futils

inp = futils.read_list("../data/day5.txt")
max_passid = 0
pass_id_list = list()
for line in inp:
    row_start, row_end = 0, 127
    col_start, col_end = 0, 7
    row, col = 0, 0
    for idx in range(6):
        mid = row_start + int((row_end - row_start)/2)
        if line[idx] == 'F':
            row_end = mid
        elif line[idx] == 'B':
            row_start = mid + (0 if mid % 2 == 0 else 1)
    if line[6] == 'F':
        row = row_start
    elif line[6] == 'B':
        row = row_end
    for idx in range(7, 9):
        mid = col_start + int((col_end - col_start) / 2)
        if line[idx] == 'L':
            col_end = mid
        elif line[idx] == 'R':
            col_start = mid + (0 if mid % 2 == 0 else 1)
    if line[9] == 'L':
        col = col_start
    elif line[9] == 'R':
        col = col_end
    pass_id = 8 * row + col
    pass_id_list.append(pass_id)
    max_passid = max(max_passid, pass_id)

pass_id_list.sort()
for idx in range(1, len(pass_id_list)):
    if pass_id_list[idx] == pass_id_list[idx - 1] + 2:
        print("Missing passID: {0}".format(pass_id_list[idx] - 1))
        break
