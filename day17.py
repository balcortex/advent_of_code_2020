from __future__ import annotations
from typing import Generator, NamedTuple, Set, Tuple, Union
import itertools

NEIGHBORS = tuple(list(itertools.product(*[[0, -1, 1]] * 3))[1:])
NEIGHBORS4 = tuple(list(itertools.product(*[[0, -1, 1]] * 4))[1:])


class Point(NamedTuple):
    x: int
    y: int
    z: int = 0
    w: int = 0

    def __add__(self, other):
        return (a + b for (a, b) in zip(self, other))

    def neighbors(self) -> Generator[Point, None, None]:
        for n in self._delta_neighbors():
            yield self.__class__(*(self + n))

    @staticmethod
    def _delta_neighbors() -> Tuple[Tuple[int]]:
        return NEIGHBORS


class Point4(Point):
    @staticmethod
    def _delta_neighbors() -> Tuple[Tuple[int]]:
        return NEIGHBORS4


class Grid:
    def __init__(self, text: str, fourth_dim: bool = False):
        make_point = Point if not fourth_dim else Point4
        self.grid: Set[Union[Point, Point4]] = {
            make_point(x, y)
            for y, row in enumerate(text.split("\n"))
            for x, char in enumerate(row)
            if char == "#"
        }

    def step(self) -> int:
        new_candidates = {
            p for point in self.grid for p in point.neighbors() if p not in self.grid
        }

        new_grid = set()

        for point in self.grid:
            n = sum(p in self.grid for p in point.neighbors())
            if n in [2, 3]:
                new_grid.add(point)

        for point in new_candidates:
            n = sum(p in self.grid for p in point.neighbors())
            if n in [3]:
                new_grid.add(point)

        self.grid = new_grid

        return len(self.grid)

    def play(self, cycles: int) -> int:
        for _ in range(cycles):
            self.step()

        return len(self.grid)


TXT = """.#.
..#
###"""
GRID = Grid(TXT)
GRID4 = Grid(TXT, fourth_dim=True)

assert GRID.play(6) == 112
assert GRID4.play(6) == 848

with open("day17.txt") as f:
    txt = f.read()

grid = Grid(txt)
grid4 = Grid(txt, fourth_dim=True)

assert grid.play(6) == 215
assert grid4.play(6) == 1728