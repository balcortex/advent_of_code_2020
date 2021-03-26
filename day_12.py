from typing import NamedTuple, Sequence

COORDS = {"E": (1, 0), "N": (0, 1), "W": (-1, 0), "S": (0, -1)}
RTURNS = {"E": "S", "S": "W", "W": "N", "N": "E"}
LTURNS = {"S": "E", "W": "S", "N": "W", "E": "N"}


class Ship:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.facing = "E"

    def move(self, s: str) -> None:
        instructions = self.parse(s)

        for dir_, value in instructions:
            if dir_ == "F":
                dirx, diry = COORDS[self.facing]
                self.posx += dirx * value
                self.posy += diry * value
            elif dir_ == "R":
                turns = value // 90
                for t in range(turns):
                    self.facing = RTURNS[self.facing]
            elif dir_ == "L":
                turns = value // 90
                for t in range(turns):
                    self.facing = LTURNS[self.facing]
            else:
                dirx, diry = COORDS[dir_]
                self.posx += dirx * value
                self.posy += diry * value

    @property
    def manhattan(self) -> int:
        return abs(self.posx) + abs(self.posy)

    @staticmethod
    def parse(s: str) -> Sequence:
        return [(s[0], int(s[1:])) for s in s.split("\n")]


assert Ship.parse("F10") == [("F", 10)]

INSTRS = """F10
N3
F7
R90
F11"""

ship = Ship()
ship.move(INSTRS)
assert ship.manhattan == 25

with open("day_12_input.txt") as f:
    ship = Ship()
    ship.move(f.read())
    print(ship.manhattan)


class Ship2:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.wp_posx = 10
        self.wp_posy = 1
        self.wp_angle = (1, 1)

    def move(self, s: str) -> None:
        instructions = self.parse(s)

        for dir_, value in instructions:
            if dir_ == "F":
                self.posx += self.wp_posx * value
                self.posy += self.wp_posy * value

            elif dir_ == "R":
                turns = value // 90
                for t in range(turns):
                    self.wp_posx, self.wp_posy = self.wp_posy, -self.wp_posx

            elif dir_ == "L":
                turns = value // 90
                for t in range(turns):
                    self.wp_posx, self.wp_posy = -self.wp_posy, self.wp_posx

            else:
                dirx, diry = COORDS[dir_]
                self.wp_posx += dirx * value
                self.wp_posy += diry * value

    @property
    def manhattan(self) -> int:
        return abs(self.posx) + abs(self.posy)

    @staticmethod
    def parse(s: str) -> Sequence:
        return [(s[0], int(s[1:])) for s in s.split("\n")]


assert Ship2.parse("F10") == [("F", 10)]

INSTRS = """F10
N3
F7
R90
F11"""

ship2 = Ship2()
ship2.move(INSTRS)
assert ship2.manhattan == 286
assert ship2.posy == -72
assert ship2.posx == 214

with open("day_12_input.txt") as f:
    ship2 = Ship2()
    ship2.move(f.read())
    print(ship2.manhattan)
