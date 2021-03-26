from typing import List
from functools import lru_cache

TXT = """16
10
15
5
1
11
7
19
6
12
4"""


def distribution(s: str) -> int:
    inps = sorted(list(map(int, s.split("\n"))))
    dif1 = [(a, b) for a, b in zip(inps[:], inps[1:]) if b - a == 1]
    dif3 = [(a, b) for a, b in zip(inps[:], inps[1:]) if b - a == 3]

    return len(dif1) + 1, len(dif3) + 1


assert distribution(TXT) == (7, 5)

with open("day_10_input.txt") as f:
    txt = f.read()
    dif1, dif3 = distribution(txt)
    print(dif1 * dif3)

# Part 2


@lru_cache(maxsize=1000)
def count_paths(lst: List[int], num: int) -> int:
    if num == 0:
        return 1

    if num not in lst:
        return 0

    if num == 1:
        return count_paths(lst, 0)

    if num == 2:
        return count_paths(lst, 1) + 1

    return (
        count_paths(lst, num - 1)
        + count_paths(lst, num - 2)
        + count_paths(lst, num - 3)
    )


assert count_paths((0, 1, 2, 3), 0) == 1
assert count_paths((0, 1, 2, 3), 2) == 2
assert count_paths((0, 1, 3), 2) == 0
assert count_paths(tuple(map(int, TXT.split("\n"))), 19) == 8


with open("day_10_input.txt") as f:
    txt = f.read()
    num = max(list(map(int, txt.split("\n"))))
    print(count_paths(tuple(map(int, txt.split("\n"))), num))
