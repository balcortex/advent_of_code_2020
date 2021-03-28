from typing import Dict, Generator, Optional, Sequence, Tuple, List


TXT = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

ranges = Tuple[range, range]


def parse_note(string: str) -> ranges:
    nums = string.split(": ")[-1]  # gives '1-3 or 5-7'
    tup_one, tup_two = nums.split(" or ")  # gives ('1-3', '5-7')
    tup_one = list(map(int, tup_one.split("-")))
    tup_two = list(map(int, tup_two.split("-")))
    tup_one[-1] += 1  # inclusie (1-3) must accept (1,2,3)
    tup_two[-1] += 1

    return range(*tup_one), range(*tup_two)


def parse_notes(string: str) -> Sequence[ranges]:
    return [rang for line in string.split("\n") for rang in parse_note(line)]


def parse_ticket(string: str) -> Tuple[int, ...]:
    return tuple(map(int, string.split(",")))


def in_ranges(num: int, ranges: Sequence[range]) -> bool:
    for rang in ranges:
        if num in rang:
            return True
    return False


def invalid(ranges: Sequence[range], ticket: Sequence[int]) -> Sequence[int]:
    no_valids = []
    for t in ticket:
        if in_ranges(t, ranges):
            continue
        no_valids.append(t)

    return no_valids


def scanner(string: str) -> int:
    notes, my_ticket, nby_tickets = string.split("\n\n")
    ranges = parse_notes(notes)

    no_valids = []
    for tick in nby_tickets.split("\n")[1:]:
        no_valids.extend(invalid(ranges, parse_ticket(tick)))

    return sum(no_valids)


assert parse_note("class: 1-3 or 5-7") == (range(1, 4), range(5, 8))
assert parse_note("row: 6-11 or 33-44") == (range(6, 12), range(33, 45))
assert parse_ticket("7,3,47") == (7, 3, 47)
assert parse_ticket("40,4,50") == (40, 4, 50)
assert parse_notes("class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50") == [
    range(1, 4),
    range(5, 8),
    range(6, 12),
    range(33, 45),
    range(13, 41),
    range(45, 51),
]
assert invalid(parse_notes("class: 1-3 or 5-7"), parse_ticket("1,4,8")) == [4, 8]

with open("day16.txt") as f:
    txt = f.read()
scanner(txt)


def is_valid_ticket(ranges: Sequence[range], ticket: Sequence[int]) -> bool:
    for t in ticket:
        if not in_ranges(t, ranges):
            return False
    return True


assert is_valid_ticket(parse_notes("class: 1-3 or 5-7"), parse_ticket("1,4,8")) == False
assert (
    is_valid_ticket(parse_notes("class: 1-3 or 5-7"), parse_ticket("1,5, 8")) == False
)
assert is_valid_ticket(parse_notes("class: 1-3 or 5-7"), parse_ticket("1,5")) == True


def get_valid_tickets(string: str) -> Sequence[Sequence[int]]:
    notes, _, nby_tickets = string.split("\n\n")
    ranges = parse_notes(notes)

    valid_tickets = []
    for tick in nby_tickets.split("\n")[1:]:
        ticket = parse_ticket(tick)
        if is_valid_ticket(ranges, ticket):
            valid_tickets.append(ticket)

    return valid_tickets


def get_possible_index(note: str, valid_tickets: Sequence[Sequence[int]]) -> int:
    ranges = parse_notes(note)
    positions = list(zip(*valid_tickets))

    index = []
    for i, pos in enumerate(positions):
        if is_valid_ticket(ranges, pos):
            index.append(i)

    return index


def find_index_len(seq: Sequence[Sequence[int]], len_: int) -> int:
    for idx, inner in enumerate(seq):
        if len(inner) == len_:
            return idx

    raise IndexError("Not found")


def get_dic(seq: List[List[int]]) -> Dict[int, int]:
    dic = {}
    for i in range(len(seq)):
        seq_idx = find_index_len(seq, i + 1)
        all_keys = seq[seq_idx]
        key = set(all_keys) - set(dic.keys())
        key = list(key)[0]
        dic[key] = seq_idx

    return dic


def get_indeces(txt: str, vals=[0, 1, 2, 3, 4, 5]) -> Sequence[int]:
    notes = txt.split("\n\n")[0].split("\n")
    valid_tickets = get_valid_tickets(txt)

    posible = [get_possible_index(note, valid_tickets) for note in notes]
    dic = get_dic(posible)

    return [key for key, val in dic.items() if val in vals]


def scaner2(txt: str) -> int:
    indices = get_indeces(txt)
    _, my_ticket, _ = txt.split("\n\n")
    my_ticket = parse_ticket(my_ticket.split("\n")[-1])

    fields = [field for i, field in enumerate(my_ticket) if i in indices]
    prod = 1
    for f in fields:
        prod *= f

    return prod


assert get_indeces(txt) == [14, 4, 2, 13, 11, 19]
assert scaner2(txt) == 3253972369789