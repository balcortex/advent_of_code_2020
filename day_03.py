# Part 1

with open("day_03_input.txt") as f:
    text = f.read()

trees = 0
for index, row in enumerate(text.split("\n")[1:], start=1):
    pos = ((3 * index)) % len(row)
    if row[pos] == "#":
        trees += 1

print()
print(f"First solution\n{trees}")
print()

# Part 2


def check_slope(map, right, down):
    trees = 0
    for index, row in enumerate(text.split("\n")[1:], start=1):
        if index % down != 0:
            continue

        if down == 1:
            pos = ((right * index)) % len(row)
        else:
            pos = ((right * index)) // down % len(row)
        if row[pos] == "#":
            trees += 1

    return trees


slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
trees = 1
for slope in slopes:
    trees *= check_slope(text, *slope)

print(f"Second solution\n{trees}")
print()