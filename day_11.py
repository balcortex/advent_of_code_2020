from typing import List

Grid = List[List[str]]

LAYOUT = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

LAYOUT2 = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

LAYOUT3 = """#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""

ADJACENDTS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def adj_coord(x, y, col_len, row_len):
    adj = [
        (x, y)
        for (x, y) in [(x - a, y - b) for (a, b) in ADJACENDTS]
        if 0 <= x < row_len and 0 <= y < col_len
    ]
    return adj


def adj_busy(grid: Grid, x: int, y: int) -> int:
    row_len = len(grid)
    col_len = len(grid[0])

    adj_seats = adj_coord(x, y, col_len, row_len)
    return sum([1 for (x, y) in adj_seats if grid[x][y] == "#"])


def step(grid: Grid) -> Grid:
    row_len = len(grid)
    col_len = len(grid[0])
    grid_ = [[c for c in row] for row in grid]

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            busy = adj_busy(grid, i, j)

            if c == "L" and busy == 0:
                grid_[i][j] = "#"
            elif c == "#" and busy >= 4:
                grid_[i][j] = "L"
            else:
                grid_[i][j] = c

    return grid_


def stable_seats(grid: Grid) -> int:
    while True:
        grid_ = step(grid)
        if grid_ == grid:
            break
        grid = grid_[:]

    return sum([1 for row in grid for c in row if c == "#"])


assert adj_coord(0, 0, 3, 3) == [(1, 1), (0, 1), (1, 0)]
assert adj_coord(2, 2, 3, 3) == [(1, 2), (2, 1), (1, 1)]
assert adj_coord(1, 1, 3, 3) == [
    (2, 2),
    (1, 2),
    (0, 2),
    (2, 1),
    (0, 1),
    (2, 0),
    (1, 0),
    (0, 0),
]

grid = [[c for c in row] for row in LAYOUT.split("\n")]
grid2 = [[c for c in row] for row in LAYOUT2.split("\n")]
grid3 = [[c for c in row] for row in LAYOUT3.split("\n")]
assert step(grid) == grid2
assert step(grid2) == grid3
assert stable_seats(grid) == 37

# with open("day_11_input.txt") as f:
#     grid = [[c for c in row] for row in f.read().split("\n")]
#     print(stable_seats(grid))


LAYOUT4 = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""

LAYOUT4_1 = """.............
.L.L.#.#.#.#.
............."""


def first_visibles_busy(grid: Grid, y: int, x: int) -> int:
    row_len = len(grid)
    col_len = len(grid[0])

    busy = 0
    for dir_x, dir_y in ADJACENDTS:
        # print("dirs", "x", dir_x, "y", dir_y)
        x_ = x
        y_ = y

        while True:
            x_ += dir_x
            y_ += dir_y
            # print("x", x_, "y", y_)

            if 0 <= y_ < row_len and 0 <= x_ < col_len:
                c = grid[y_][x_]
                # print(f"{c=}")

                if c == "#":
                    busy += 1
                    break

                elif c == "L":
                    break

                else:
                    pass

            else:
                break

    return busy


grid4 = [[c for c in row] for row in LAYOUT4.split("\n")]
print(grid4[4][3])
grid4_1 = [[c for c in row] for row in LAYOUT4_1.split("\n")]
assert first_visibles_busy(grid4, 4, 3) == 8
# assert first_visibles_busy(grid4_1, 3, 4) == 8


def step2(grid: Grid) -> Grid:
    row_len = len(grid)
    col_len = len(grid[0])
    grid_ = [[c for c in row] for row in grid]

    for j, row in enumerate(grid):
        for i, c in enumerate(row):
            busy = first_visibles_busy(grid, j, i)

            if c == "L" and busy == 0:
                grid_[j][i] = "#"
            elif c == "#" and busy >= 5:
                grid_[j][i] = "L"
            else:
                grid_[j][i] = c

    return grid_


def stable_seats2(grid: Grid) -> int:
    while True:
        grid_ = step2(grid)
        if grid_ == grid:
            break
        grid = grid_[:]

    return sum([1 for row in grid for c in row if c == "#"])


LAYOUT5 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

LAYOUT6 = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

LAYOUT7 = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""

LAYOUT8 = """#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#"""

LAYOUT9 = """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#"""


grid5 = [[c for c in row] for row in LAYOUT5.split("\n")]
grid6 = [[c for c in row] for row in LAYOUT6.split("\n")]
grid7 = [[c for c in row] for row in LAYOUT7.split("\n")]
grid8 = [[c for c in row] for row in LAYOUT8.split("\n")]
grid9 = [[c for c in row] for row in LAYOUT9.split("\n")]
assert step2(grid5) == grid6
assert step2(grid6) == grid7
assert step2(grid7) == grid8
assert step2(grid8) == grid9
assert stable_seats2(grid5) == 26

with open("day_11_input.txt") as f:
    grid = [[c for c in row] for row in f.read().split("\n")]
    print(stable_seats2(grid))