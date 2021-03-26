from typing import List


def find_last_two_index(num: int, lst: List[int]) -> List[int]:
    return [idx for (idx, lst_num) in enumerate(lst) if lst_num == num][-2:]


def speak(lst: List[int]) -> List[int]:
    last_idx = len(lst) - 1  # 2
    last_num = lst[-1]  # 6
    first_idx = lst.index(last_num)  # 2

    if last_idx == first_idx:
        lst.append(0)
    else:
        idxs = find_last_two_index(last_num, lst)
        lst.append(idxs[-1] - idxs[-2])

    return lst


def play(init_seq: List[int], turns: int) -> int:
    seq = init_seq[:]
    turns -= len(init_seq)
    for i in range(0, turns):
        if i % 1_000 == 0:
            print(f"Done {i}/{turns}")
        seq = speak(seq)
    return seq[-1]


assert find_last_two_index(0, [0, 3, 6, 0]) == [0, 3]
assert find_last_two_index(3, [0, 3, 6, 0, 3, 3]) == [4, 5]
assert speak([0, 3, 6]) == [0, 3, 6, 0]
assert speak([0, 3, 6, 0]) == [0, 3, 6, 0, 3]
assert speak([0, 3, 6, 0, 3]) == [0, 3, 6, 0, 3, 3]
assert speak([0, 3, 6, 0, 3, 3]) == [0, 3, 6, 0, 3, 3, 1]
assert play([0, 3, 6], 2020) == 436
assert play([1, 3, 2], 2020) == 1

print(play([12, 1, 16, 3, 11, 0], 2020))

assert play([1, 3, 2], 30000000) == 175594
