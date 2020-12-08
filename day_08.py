with open("day_08_input.txt") as f:
    txt = f.read()

# - - - Part 1 - - -


def acum(txt: str) -> int:
    counter = 0
    index = 0
    memo = []
    program = txt.split("\n")

    while True:
        ins, num = program[index].split()
        num = int(num)

        if index not in memo:
            memo.append(index)
        else:
            break

        if ins == "nop":
            index += 1
            continue
        elif ins == "acc":
            index += 1
            counter += num
        else:
            index += num

    return counter


print()
print("First solution")
print(acum(txt))
print()


def fix(txt: str) -> int:
    counter = 0
    index = 0
    memo = []
    changed_index = 0
    program = txt.split("\n")

    while True:
        if index >= len(program):
            break

        ins, num = program[index].split()
        num = int(num)

        if index not in memo:
            memo.append(index)
        else:
            counter = 0
            index = 0
            memo = []
            program = txt.split("\n")

            while "acc" in program[changed_index]:
                changed_index += 1

            if program[changed_index].split()[0] == "nop":
                program[changed_index] = "jmp" + program[changed_index][3:]
            else:
                program[changed_index] = "nop" + program[changed_index][3:]
            changed_index += 1
            continue

        if ins == "nop":
            index += 1
            continue
        elif ins == "acc":
            index += 1
            counter += num
        else:
            index += num

    return counter


print("Second solution")
print(fix(txt))
print()