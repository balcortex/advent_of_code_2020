from typing import Any, Dict, Sequence, Union


def make_rules(string: str) -> Dict[int, Union[Sequence[int], str]]:
    dic = dict()
    for line in string.split("\n\n")[0].split("\n"):
        dic.update(parse_rule(line))
    return dic


def parse_rule(string: str) -> Dict[int, Union[Sequence[int], str]]:
    key, val = string.split(":")
    key = int(key)
    val = val.strip(' "')

    if val in "ab":
        return {key: val}

    # '2 3 | 3 2' -> [[2, 3], [3, 2]]
    seq = [list(map(int, v.split())) for v in val.split(" | ")]
    return {key: seq}


assert parse_rule("0: 4 1 5") == {0: [[4, 1, 5]]}
assert parse_rule("1: 2 3 | 3 2") == {1: [[2, 3], [3, 2]]}


TXT = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

rules = make_rules(TXT)


def get_match(rules: Dict[Any, Any], key: int):
    matches = rules[key]

    if isinstance(matches, str):
        return matches

    s = []
    for match in matches:
        s_ = []
        for m in match:
            m_ = get_match(rules, m)
            s_.append(m_)

        s.append(s_)

    try:
        s = ["".join(a) for a in s]
    except:
        pass

    return s

def comb(seq: Sequence[Sequence[Sequence[str]]]) -> Sequence[str]:
    res = []
    for inner in seq:
        for a,b in zip(*inner):
            

        

def decode_match(seq):
    m = []
    for s in seq:
        if isinstance(s, str):
            m.append(s)
            continue



a, b, c = get_match(rules, 0)[0]
