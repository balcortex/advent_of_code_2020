from typing import Sequence
from operator import sub
from collections import deque, defaultdict


class Recitation:
    def __init__(self, init_seq: Sequence[int]):
        len_ = len(init_seq)
        self.turn = len_
        self.last_spoken = init_seq[-1]
        self.dic = defaultdict(lambda: deque([0, 0], maxlen=2))

        for idx, s in zip(range(1, len_ + 1), init_seq):
            self.dic[s].append(idx)

    def speak(self) -> int:
        if 0 in self.dic[self.last_spoken]:
            self.last_spoken = 0
        else:
            self.last_spoken = abs(sub(*self.dic[self.last_spoken]))

        self.turn += 1
        self.dic[self.last_spoken].append(self.turn)

        return self.last_spoken

    def play(self, turn: int) -> int:
        while self.turn < turn:
            if self.turn % 1000000 == 0:
                print(f"Turn {self.turn}/{turn}")
            self.speak()

        return self.last_spoken


# rec = Recitation([0, 3, 6])
# assert rec.speak() == 0
# assert rec.speak() == 3
# assert rec.speak() == 3
# assert rec.speak() == 1
# assert rec.speak() == 0
# assert rec.speak() == 4
# assert rec.speak() == 0
# assert rec.play(2020) == 436

# rec = Recitation([12, 1, 16, 3, 11, 0])
# assert rec.play(30000000) == 37385
