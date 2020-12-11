import utils.fileutils as futils
from heapq import heappop, heappush

inp = futils.read_list("../data/day10.txt")
heap = list()
for line in inp:
    heappush(heap, int(line))

prev_elem = 0
one_jolts, three_jolts = 0, 0
while heap:
    curr_elem = heappop(heap)
    if curr_elem - prev_elem <= 3:
        if curr_elem - prev_elem == 1:
            one_jolts += 1
        elif curr_elem - prev_elem == 3:
            three_jolts += 1
        prev_elem = curr_elem
    else:
        print("ERROR")
        break
three_jolts += 1
print(one_jolts * three_jolts)
