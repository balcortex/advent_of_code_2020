from typing import Dict, List

TXT = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

with open("day_07_input.txt") as f:
    txt = f.read()


def parse(txt: str) -> Dict[str, str]:
    dic_bags = {}
    for line in txt.split("\n"):
        bag, content = line.split("contain")
        bag = bag.split("bags")[0].strip()
        content = content.replace("bags", "bag")
        content = content.replace(".", "")
        content = content.split("bag")
        dic_bags[bag] = []
        for inner_bag in content:
            if inner_bag == "":
                continue
            elif inner_bag == " no other ":
                continue
            else:
                inner_bag = inner_bag[3:].strip()
                dic_bags[bag].append(inner_bag)
    return dic_bags


def find_bags(dic_bags: Dict[str, str], target_bag: str) -> List[str]:
    possible_bags = []
    for bag, content in dic_bags.items():
        if target_bag in content:
            possible_bags.append(bag)

    for pos_bag in possible_bags:
        pos_bags = find_bags(dic_bags, pos_bag)
        for a in pos_bags:
            if a not in possible_bags:
                possible_bags.extend(pos_bags)

    return set(possible_bags)


# dic_bags = parse(txt)
# found = find_bags(dic_bags, "shiny gold")
# print()
# print("First solution")
# print(len(found))
# print()


def parse2(txt: str) -> Dict[str, str]:
    dic_bags = {}
    for line in txt.split("\n"):
        bag, content = line.split("contain")
        bag = bag.split("bags")[0].strip()
        content = content.replace("bags", "bag")
        content = content.replace(".", "")
        content = content.replace(",", "")
        content = content.split("bag")
        dic_bags[bag] = {}
        for inner_bag in content:
            if inner_bag == "":
                continue
            elif inner_bag == " no other ":
                continue
            else:
                inner_bag = inner_bag.strip()
                num = int(inner_bag[0])
                inner_bag = inner_bag[2:].strip()
                dic_bags[bag][inner_bag] = num
    return dic_bags


def bags_in_bag(dic_bags: Dict[str, int], bag: str) -> int:
    # If no other bag inside, return 0
    if dic_bags[bag] == {}:
        return 0

    num_bags = 0
    for inner_bag, number in dic_bags[bag].items():
        num_bags += (bags_in_bag(dic_bags, inner_bag) + 1) * number
    return num_bags


dic_bags = parse2(txt)
print("Second solution")
print(bags_in_bag(dic_bags, "shiny gold"))
