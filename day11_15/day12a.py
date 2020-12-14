import utils.fileutils as futils
from heapq import heappop, heappush

inp = futils.read_list("../data/day12.txt")
degree, horizontal, vertical = 0, 0, 0
for line in inp:
    action = line[0]
    val = int(line[1:])
    if action == "N":
        vertical += val
    elif action == "S":
        vertical -= val
    elif action == "E":
        horizontal += val
    elif action == "W":
        horizontal -= val
    elif action == "L":
        degree += val
        if degree >= 360:
            degree %= 360
    elif action == "R":
        degree -= val
        if degree < 0:
            degree += 360
    elif action == "F":
        if degree == 0:
            horizontal += val
        elif degree == 90:
            vertical += val
        elif degree == 180:
            horizontal -= val
        elif degree == 270:
            vertical -= val
        else:
            print("360 NOT POSSIBLE")
    else:
        print("Wrong INPUT")

print(horizontal, vertical, abs(horizontal) + abs(vertical))