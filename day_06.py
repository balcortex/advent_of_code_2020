from collections import Counter

with open("day_06_input.txt") as f:
    txt = f.read()

# - - - Part 1 - - -
def group_generator(string: str):
    # Split into groups
    for group in string.split("\n\n"):
        ans = []
        # Split into persons
        for people in group.split("\n"):
            ans.append(people)
        # Combine all answers into a single string, to later create a set
        yield list(set("".join(ans)))


def count(raw: str):
    groups = group_generator(raw)
    counter = 0
    for group in groups:
        # The group contains one letter per answer, so just we just need to get
        # the length of the group
        counter += len(group)
    return counter


print()
print("First Solution")
print(count(txt))
print()

# - - - Part 2 - - -
def group_generator_2(string: str):
    # Split into groups
    for group in string.split("\n\n"):
        ans = []
        # Split into persons
        for people in group.split("\n"):
            ans.append(people)
        # Combine all answers and return the number of persons who responded
        yield "".join(ans), len(ans)


def count_2(raw: str):
    groups = group_generator_2(raw)
    counts = 0
    for group, size in groups:
        # Create a dict mapping keys (letters) with the number of occurrences
        counter = Counter(group)
        # We just need to know how many occurences of any letter is equal
        # to the number of people who responded
        for ans_num in counter.values():
            if ans_num == size:
                counts += 1
    return counts


print("Second Solution")
print(count_2(txt))
print()