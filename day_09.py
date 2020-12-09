from typing import Deque, List
from collections import deque

with open(f"day_09_input.txt") as f:
    txt = f.read()


TXT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def is_next_valid(seq: List, num: int) -> bool:
    valids = {a + b for a in seq for b in seq[1:]}
    return num in valids


def preamble_gen(txt: str, preamble: int) -> List:
    lst = deque(maxlen=preamble + 1)
    for line in txt.split("\n"):
        lst.append(int(line))

        if len(lst) == preamble + 1:
            yield list(lst)[:-1], lst[-1]


def attack(preamble_gen) -> int:
    for lst, nxt in preamble_gen:
        if not is_next_valid(lst, nxt):
            return nxt


assert is_next_valid([35, 20, 15, 25, 47], 40)
assert not is_next_valid([102, 117, 150, 182, 95], 127)

pre_gen = preamble_gen(txt, 25)
ans1 = attack(pre_gen)

print()
print("First solution")
print(ans1)
print()


def range_gen(lst: List, size: int, stop_at: int) -> List:
    deq = deque(maxlen=size)
    for num in lst:
        deq.append(int(num))

        if deq[-1] == stop_at:
            break

        if len(deq) == size:
            yield list(deq)


def find_contiguos_range(txt: str, num: int):
    lst = txt.split("\n")

    size = 1
    while True:
        size += 1  # start with length 2
        ran_gen = range_gen(lst, size, num)

        for tup in ran_gen:
            if sum(tup) == num:
                return min(tup) + max(tup)


print("Second solution")
print(find_contiguos_range(txt, ans1))
print()
