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
            i, j = -1, -1
            while row + i >= 0 and col + j >= 0:
                if grid[row + i][col + j] == ".":
                    i -= 1
                    j -= 1
                    continue
                else:
                    if grid[row + i][col + j] == "#":
                        count += 1
                    break

            i = -1
            while row + i >= 0:
                if grid[row + i][col] == ".":
                    i -= 1
                    continue
                else:
                    if grid[row + i][col] == "#":
                        count += 1
                    break

            i, j = -1, 1
            while row + i >= 0 and col + j < cols:
                if grid[row + i][col + j] == ".":
                    i -= 1
                    j += 1
                    continue
                else:
                    if grid[row + i][col + j] == "#":
                        count += 1
                    break

            # Same level
            j = -1
            while col + j >= 0:
                if grid[row][col + j] == ".":
                    j -= 1
                    continue
                else:
                    if grid[row][col + j] == "#":
                        count += 1
                    break

            j = 1
            while col + j < cols:
                if grid[row][col + j] == ".":
                    j += 1
                    continue
                else:
                    if grid[row][col + j] == "#":
                        count += 1
                    break

            # Lower Level
            i, j = 1, -1
            while row + i < rows and col + j >= 0:
                if grid[row + i][col + j] == ".":
                    i += 1
                    j -= 1
                    continue
                else:
                    if grid[row + i][col + j] == "#":
                        count += 1
                    break

            i = 1
            while row + i < rows:
                if grid[row + i][col] == ".":
                    i += 1
                    continue
                else:
                    if grid[row + i][col] == "#":
                        count += 1
                    break

            i, j = 1, 1
            while row + i < rows and col + j < cols:
                if grid[row + i][col + j] == ".":
                    i += 1
                    j += 1
                    continue
                else:
                    if grid[row + i][col + j] == "#":
                        count += 1
                    break

            if grid[row][col] == "L":
                if count == 0:
                    new_grid[row] += "#"
                    changes_count += 1
                    occupied_seats += 1
                else:
                    new_grid[row] += "L"
            elif grid[row][col] == "#":
                if count >= 5:
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
