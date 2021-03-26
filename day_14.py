from typing import Sequence, Tuple
import itertools


class Docker:
    def __init__(self):
        self.memory = {}

    def initialize(self, string: str) -> None:
        for line in string.split("\n"):
            if line.startswith("mask"):
                self.mask = Docker.parse_mask(line)
            elif line.startswith("mem"):
                mem, code = Docker.parse_mem(line)
                self.memory[mem] = Docker.apply_mask(code, self.mask)

    def sum_vals(self) -> int:
        return sum(val for val in self.memory.values())

    @staticmethod
    def apply_mask(num: int, mask: str) -> int:
        bin_ = f"{num:036b}"
        new_bin = ""
        for bit_mask, bit_bin in zip(mask, bin_):
            if bit_mask == "X":
                new_bin += bit_bin
                continue
            new_bin += bit_mask

        return int(new_bin, 2)

    @staticmethod
    def parse_mask(string: str) -> str:
        return string[7:]

    def parse_mem(string: str) -> Tuple[int, int]:
        mem, code = string.split(" = ")
        mem = mem.split("[")[-1][:-1]

        return int(mem), int(code)


assert Docker.apply_mask(11, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 73
assert Docker.apply_mask(101, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 101
assert Docker.apply_mask(0, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 64
assert (
    Docker.parse_mask("mask = 0111X10100100X1111X10010X000X1000001")
    == "0111X10100100X1111X10010X000X1000001"
)
assert Docker.parse_mem("mem[50907] = 468673978") == (50907, 468673978)

with open("day_14.txt") as f:
    txt = f.read()

dock = Docker()
dock.initialize(txt)
dock.sum_vals()


class Docker2:
    def __init__(self):
        self.memory = {}

    def initialize(self, string: str) -> None:
        for line in string.split("\n"):
            if line.startswith("mask"):
                self.mask = Docker2.parse_mask(line)
            elif line.startswith("mem"):
                mem, code = Docker2.parse_mem(line)
                floating_mem = Docker2.apply_mask(mem, self.mask)
                mems = Docker2.comb_floating(floating_mem)
                for mem in mems:
                    self.memory[mem] = code

    def sum_vals(self) -> int:
        return sum(val for val in self.memory.values())

    @staticmethod
    def comb_floating(string: str) -> Sequence[int]:
        count = string.count("X")
        string = string.replace("X", "{}")
        combs = itertools.product(*([["0", "1"]] * count))

        return (int(string.format(*comb), 2) for comb in combs)

    @staticmethod
    def apply_mask(num: int, mask: str) -> int:
        bin_ = f"{num:036b}"
        new_bin = ""
        for bit_mask, bit_bin in zip(mask, bin_):
            if bit_mask == "0":
                new_bin += bit_bin
                continue
            new_bin += bit_mask

        return new_bin

    @staticmethod
    def parse_mask(string: str) -> str:
        return string[7:]

    def parse_mem(string: str) -> Tuple[int, int]:
        mem, code = string.split(" = ")
        mem = mem.split("[")[-1][:-1]

        return int(mem), int(code)


assert (
    Docker2.apply_mask(42, "000000000000000000000000000000X1001X")
    == "000000000000000000000000000000X1101X"
)
assert tuple(Docker2.comb_floating("000000000000000000000000000000X1101X")) == (
    26,
    27,
    58,
    59,
)

dock2 = Docker2()
dock2.initialize(txt)
dock2.sum_vals()