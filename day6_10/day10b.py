import utils.fileutils as futils
from heapq import heappop, heappush

inp = futils.read_list("../data/day10.txt")
heap = []
for line in inp:
    heappush(heap, int(line))

heap_list = [0]
while heap:
    heap_list.append(heappop(heap))
res_list = [0]*len(heap_list)
res_list[0] = 1
idx = 0
count = 1
while idx < len(heap_list) - 1:
    if idx + 3 < len(heap_list) and heap_list[idx + 3] - heap_list[idx] <= 3:
        res_list[idx + 3] += res_list[idx]
    if idx + 2 < len(heap_list) and heap_list[idx + 2] - heap_list[idx] <= 3:
        res_list[idx + 2] += res_list[idx]
    if idx + 1 < len(heap_list) and heap_list[idx + 1] - heap_list[idx] <= 3:
        res_list[idx + 1] += res_list[idx]
    idx += 1

print(res_list[-1])
