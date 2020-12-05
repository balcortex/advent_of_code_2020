from typing import Sequence

# Part 1


def decode_str(string: str) -> int:
    if len(string) == 7:
        rows = range(0, 128)
    else:
        rows = range(0, 8)

    for char in string:
        half = len(rows) // 2
        if char in "FL":
            rows = rows[:half]
        else:
            rows = rows[half:]

    return int(list(rows)[0])


def get_id(string: str) -> int:
    str1 = string[:7]
    str2 = string[7:]

    return decode_str(str1) * 8 + decode_str(str2)


def get_ids(string: str) -> Sequence[int]:
    encoded = string.split()
    ids = []
    for s in encoded:
        ids.append(get_id(s))
    return ids


with open("day_05_input.txt") as f:
    txt = f.read()

print()
print("First solution")
print(max(get_ids(txt)))
print()

# Part 2

taken_ids = set(get_ids(txt))
all_ids = set(range(min(taken_ids), max(taken_ids) + 1))

print("Second solution")
print(all_ids.difference(taken_ids).pop())
print()
