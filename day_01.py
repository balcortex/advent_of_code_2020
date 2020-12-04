with open("day_01_input.txt") as f:
    text = f.read()

nums = [int(a) for a in text.split()]


# Part 1
solved = False
for num1 in nums:
    for num2 in nums:
        if num1 + num2 == 2020:
            solved = True
            break
    if solved:
        break

print()
print(f"First solution\n{num1*num2}")


# Part 2
solved = False
for num1 in nums:
    for num2 in nums:
        for num3 in nums:
            if num1 + num2 + num3 == 2020:
                solved = True
                break
        if solved:
            break
    if solved:
        break

print()
print(f"Second solution\n{num1*num2*num3}")
print()
