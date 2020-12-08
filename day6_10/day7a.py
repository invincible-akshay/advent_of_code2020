import utils.fileutils as futils

inp = futils.read_list("../data/day7.txt")
colors_dict = dict()
for line in inp:
    line_splits = line.split(" bags contain ")
    parent, children = line_splits[0], line_splits[1][:-1]
    childs = children.split(", ")
    for child in childs:
        start_idx = 0
        while child[start_idx].isnumeric():
            start_idx += 1
        start_idx += 1
        if child[-1] == 's':
            end_idx = -5
        else:
            end_idx = -4
        color = child[start_idx:end_idx]
        if color in colors_dict:
            colors_dict[color].append(parent)
        else:
            colors_dict[color] = [parent]

visited_set = set()
queue = list()
queue.append("shiny gold")
while queue:
    curr_color = queue.pop()
    parents = colors_dict.get(curr_color)
    if parents is not None:
        for _parent in parents:
            if _parent not in visited_set:
                queue.append(_parent)
    visited_set.add(curr_color)

print("{0} bags".format(len(visited_set) - 1))
