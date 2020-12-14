import utils.fileutils as futils


def get_quadrant(hor, ver):
    if hor >= 0:
        if ver >= 0:
            return 1
        else:
            return 4
    else:
        if ver >= 0:
            return 2
        else:
            return 3


def change_quadrant(hor, ver, old_q, new_q):
    if new_q == old_q:
        return hor, ver
    quad_dict = {1: (1, 1), 2: (-1, 1), 3: (-1, -1), 4: (1, -1)}
    diff = (new_q - old_q) % 2
    hor, ver = abs(hor), abs(ver)
    if diff != 0:
        ver, hor = hor, ver
    return hor * quad_dict[new_q][0], ver * quad_dict[new_q][1]


inp = futils.read_list("../data/day12.txt")
horizontal, vertical = 10, 1
ship_horizontal, ship_vertical = 0, 0
for line in inp:
    print(line)
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
        quad = get_quadrant(horizontal, vertical)
        val %= 360
        if val == 0:
            continue
        new_quad = quad + (val // 90)
        if new_quad > 4:
            new_quad -= 4
        print(quad, new_quad)
        horizontal, vertical = change_quadrant(horizontal, vertical, quad, new_quad)
    elif action == "R":
        quad = get_quadrant(horizontal, vertical)
        val %= 360
        if val == 0:
            continue
        new_quad = quad + (4 - (val // 90))
        if new_quad > 4:
            new_quad -= 4
        print(quad, new_quad)
        horizontal, vertical = change_quadrant(horizontal, vertical, quad, new_quad)
    elif action == "F":
        ship_horizontal += val*horizontal
        ship_vertical += val*vertical
    else:
        print("Wrong INPUT")
    print(horizontal, vertical)

print(ship_horizontal, ship_vertical, abs(ship_horizontal) + abs(ship_vertical))
