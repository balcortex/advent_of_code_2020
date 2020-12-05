from typing import Dict, Sequence

# Part 1

with open("day_04_input.txt") as f:
    txt = f.read()


def get_next_passport(txt: str) -> str:
    passport = []
    for line in txt.split("\n"):
        if line:
            passport.append(line)
        else:
            yield to_dict((" ").join(passport))
            passport = []


def to_dict(passport: str) -> Dict[str, str]:
    return {key: value for key, value in (pair.split(":") for pair in passport.split())}


def check_keys(pass_dic: Dict[str, str], valid_keys: Sequence[str]) -> bool:
    pass_keys = pass_dic.keys()
    for key in valid_keys:
        if key not in pass_keys:
            return False
    return True


def count_valid_passports(txt: str, valid_keys: Sequence[str]) -> int:
    passport_gen = get_next_passport(txt)
    valid = 0
    for passport in passport_gen:
        if check_keys(passport, valid_keys):
            valid += 1
    return valid


valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
print()
print("First solution")
print(count_valid_passports(txt, valid_keys))
print()


# Part 2


def check_byr(year: str) -> bool:
    if 1920 <= int(year) <= 2002:
        return True
    return False


def check_iyr(year: str) -> bool:
    if 2010 <= int(year) <= 2020:
        return True
    return False


def check_eyr(year: str) -> bool:
    if 2020 <= int(year) <= 2030:
        return True
    return False


def check_hgt(height: str) -> bool:
    if "in" in height:
        num = height.split("in")[0]

        if 59 <= int(num) <= 76:
            return True

    if "cm" in height:
        num = height.split("cm")[0]

        if 150 <= int(num) <= 193:
            return True

    return False


def check_hcl(color: str) -> bool:
    if color[0] != "#":
        return False

    if len(color) != 7:
        return False

    for a in color[1:]:
        if a not in "abcdef0123456789":
            return False

    return True


def check_ecl(color: str) -> bool:
    if color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True

    return False


def check_pid(pid: str) -> bool:
    if len(pid) != 9:
        return False
    return True


def check_cid(cid: str) -> bool:
    return True


check_fns = {
    "byr": check_byr,
    "iyr": check_iyr,
    "eyr": check_eyr,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": check_ecl,
    "pid": check_pid,
    "cid": check_cid,
}


def count_valid_passports_2(txt: str, valid_keys: Sequence[str]) -> int:
    passport_gen = get_next_passport(txt)
    valid = 0
    for passport in passport_gen:
        if not check_keys(passport, valid_keys):
            continue
        if all([check_fns[key](value) for key, value in passport.items()]):
            valid += 1
    return valid


print("Second solution")
print(count_valid_passports_2(txt, valid_keys))
print()
