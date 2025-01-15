import itertools
import functools
import operator

op_map = {"+": operator.add, "*": operator.mul}


def inner_operation(string: str) -> str:
    all_elems = string.strip("()").split()
    nums = map(int, filter(lambda c: c not in "+*", all_elems))
    ops = iter(filter(lambda c: c in "+*", all_elems))

    result = itertools.accumulate(nums, lambda *num_tup: op_map[next(ops)](*num_tup))

    return str(list(result)[-1])


def find_inner_parentheses(string: str) -> str:
    first_idx = 0
    for idx, c in enumerate(string):
        if c == "(":
            first_idx = idx
        elif c == ")":
            return string[first_idx : idx + 1]


def operation(string: str) -> int:
    while "(" in string:
        inner = find_inner_parentheses(string)
        string = string.replace(inner, inner_operation(inner))

    return inner_operation(string)


assert inner_operation("(1 + 2 * 3)") == "9"
assert inner_operation("((1 + 2 * 3))") == "9"
assert inner_operation("1 + 2 * 3") == "9"
assert find_inner_parentheses("((1 + 2 * 3))") == "(1 + 2 * 3)"
assert find_inner_parentheses("(1 + 2 * 3)") == "(1 + 2 * 3)"
assert operation("1 + (2 * 3) + (4 * (5 + 6))") == "51"
assert operation("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == "13632"

with open("day18.txt") as f:
    txt = f.read()
    lines = [operation(line) for line in txt.split("\n")]
    sum_ = sum(map(int, lines))
    assert sum_ == 86311597203806


def inner_operation2(string: str) -> str:
    string = string.strip("()")
    string += " * 0"

    all_elems = string.split()
    new_elems = []

    last_num = int(all_elems.pop(0))
    for op, num in zip(all_elems[::2], all_elems[1::2]):
        if op == "*":
            new_elems.append(last_num)
            last_num = int(num)
        elif op == "+":
            last_num += int(num)
        else:
            raise NotImplementedError

    return str(functools.reduce(operator.mul, new_elems, 1))


def operation2(string: str) -> int:
    while "(" in string:
        inner = find_inner_parentheses(string)
        string = string.replace(inner, inner_operation2(inner))

    return inner_operation2(string)


assert inner_operation2("1 + 2 * 3 + 4 * 5 + 6") == str(3 * 7 * 11)
assert inner_operation2("3 * 7 * 11") == str(3 * 7 * 11)
assert inner_operation2("3 * 7 * 11 + 1") == str(3 * 7 * 12)
assert operation2("1 + (2 * 3) + (4 * (5 + 6))") == "51"
assert operation2("1 + 2 * 3 + 4 * 5 + 6") == "231"


with open("day18.txt") as f:
    txt = f.read()
    lines = [operation2(line) for line in txt.split("\n")]
    sum_ = sum(map(int, lines))
    assert sum_ == 276894767062189