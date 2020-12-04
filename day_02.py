"""
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given letter
must appear for the password to be valid. For example, 1-3 a means that the
password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not;
it contains no instances of b, but needs at least 1. The first and third
passwords are valid: they contain one a or nine c, both within the limits of
their respective policies.

How many passwords are valid according to their policies?
"""

with open("day_02_input.txt") as f:
    text = f.read()

valid = 0
for a in text.split("\n"):
    limits, letter, password = a.split()
    min_, max_ = [int(b) for b in limits.split("-")]
    letter = letter.split(":")[0]
    letter_count = password.count(letter)
    if min_ <= letter_count <= max_:
        valid += 1

print()
print(f"First solution\n{valid}")


"""
Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

valid = 0
for a in text.split("\n"):
    limits, letter, password = a.split()
    pos1, pos2 = [int(b) for b in limits.split("-")]
    letter = letter.split(":")[0]
    letter_in_pos1 = password[pos1 - 1] == letter
    letter_in_pos2 = password[pos2 - 1] == letter
    if not letter_in_pos1 == letter_in_pos2:
        valid += 1


print()
print(f"Second solution\n{valid}")
print()
