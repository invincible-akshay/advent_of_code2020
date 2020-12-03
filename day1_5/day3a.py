import utils.fileutils as futils

inp = futils.read_list("../data/day3.txt")
tree_count = 0
right_move, down_move = 3, 1
curr_x, curr_y = 0, 0
while curr_y < len(inp):
    if inp[curr_y][curr_x] == '#':
        tree_count += 1
    curr_x = (curr_x + right_move) % len(inp[curr_y])
    curr_y += down_move

print("Total trees = {0}".format(tree_count))
