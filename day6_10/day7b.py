import utils.fileutils as futils

inp = futils.read_list("../data/day7.txt")
colors_dict = dict()
for line in inp:
    line_splits = line.split(" bags contain ")
    parent, children = line_splits[0], line_splits[1][:-1]
    if children != "no other bags":
        childs = children.split(", ")
        for child in childs:
            start_idx = 0
            while child[start_idx].isnumeric():
                start_idx += 1
            count = int(child[:start_idx])
            start_idx += 1
            if child[-1] == 's':
                end_idx = -5
            else:
                end_idx = -4
            color = child[start_idx:end_idx]
            if parent in colors_dict:
                colors_dict[parent].append((color, count))
            else:
                colors_dict[parent] = [(color, count)]

bags_count = 0
inners = colors_dict["shiny gold"]
for inner in inners:
    bags_count += inner[1]
    if inner[0] in colors_dict:
        for _inner in colors_dict[inner[0]]:
            _inner_color, _inner_count = _inner[0], _inner[1]
            inners.append((_inner_color, inner[1]*_inner_count))


print("{0} bags".format(bags_count))
