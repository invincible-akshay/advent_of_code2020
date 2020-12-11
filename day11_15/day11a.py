import utils.fileutils as futils
from heapq import heappop, heappush

inp = futils.read_list("../data/day11.txt")
grid = list()
for line in inp:
    grid.append(line)

rows, cols = len(grid), len(grid[0])

occupied_seats = 0
while True:
    changes_count = 0
    new_grid = list()
    for row in range(rows):
        new_grid.append("")
        for col in range(cols):
            if grid[row][col] == ".":
                new_grid[row] += "."
                continue
            count = 0
            if row - 1 >= 0:
                if col - 1 >= 0:
                    if grid[row - 1][col - 1] == "#":
                        count += 1
                if grid[row - 1][col] == "#":
                    count += 1
                if col + 1 < cols:
                    if grid[row - 1][col + 1] == "#":
                        count += 1

            if col - 1 >= 0:
                if grid[row][col - 1] == "#":
                    count += 1
            if col + 1 < cols:
                if grid[row][col + 1] == "#":
                    count += 1

            if row + 1 < rows:
                if col - 1 >= 0:
                    if grid[row + 1][col - 1] == "#":
                        count += 1
                if grid[row + 1][col] == "#":
                    count += 1
                if col + 1 < cols:
                    if grid[row + 1][col + 1] == "#":
                        count += 1
            if grid[row][col] == "L":
                if count == 0:
                    new_grid[row] += "#"
                    changes_count += 1
                    occupied_seats += 1
                else:
                    new_grid[row] += "L"
            elif grid[row][col] == "#":
                if count >= 4:
                    new_grid[row] += "L"
                    changes_count += 1
                else:
                    occupied_seats += 1
                    new_grid[row] += "#"
    grid = new_grid
    if changes_count == 0:
        break
    occupied_seats = 0

print(occupied_seats)
