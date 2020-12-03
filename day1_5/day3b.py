import utils.fileutils as futils

inp = futils.read_list("../data/day3.txt")
moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
final_res = 1
for right_move, down_move in moves:
    curr_x, curr_y = 0, 0
    tree_count = 0
    while curr_y < len(inp):
        if inp[curr_y][curr_x] == '#':
            tree_count += 1
        curr_x = (curr_x + right_move) % len(inp[curr_y])
        curr_y += down_move
    final_res *= tree_count

print("Total trees product = {0}".format(final_res))
