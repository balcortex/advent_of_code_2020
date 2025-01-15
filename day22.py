from __future__ import annotations
from typing import Dict, List, NamedTuple, Sequence
import time
import sys


class CrabCombat(NamedTuple):
    p1: List[int]
    p2: List[int]

    @classmethod
    def from_string(cls, string: str) -> CrabCombat:
        p1, p2 = string.split("\n\n")
        p1 = list(map(int, p1.split("\n")[1:]))
        p2 = list(map(int, p2.split("\n")[1:]))

        return CrabCombat(p1, p2)

    def turn(self):
        p1_card = self.p1.pop(0)
        p2_card = self.p2.pop(0)

        if p1_card > p2_card:
            self.p1.extend([p1_card, p2_card])
        elif p2_card > p1_card:
            self.p2.extend([p2_card, p1_card])

    def play(self) -> int:
        turn = 0
        while self.p1 and self.p2:
            self.turn()
            turn += 1

        return turn

    @property
    def winner(self) -> List[int]:
        return self.p1 if self.p1 else self.p2

    @property
    def score(self) -> int:
        return sum(
            pos * card for pos, card in enumerate(reversed(self.winner), start=1)
        )


TXT = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


crab = CrabCombat.from_string(TXT)
crab.play()
assert crab.score == 306


with open("day22.txt") as f:
    txt = f.read()
    crab = CrabCombat.from_string(txt)
    crab.play()
    assert crab.score == 36257


class CrabCombat2(NamedTuple):
    p1: List[int]
    p2: List[int]
    history: List[List[int]] = []
    game: Sequence[int] = [0]

    @classmethod
    def from_string(cls, string: str) -> CrabCombat2:
        p1, p2 = string.split("\n\n")
        p1 = list(map(int, p1.split("\n")[1:]))
        p2 = list(map(int, p2.split("\n")[1:]))

        return CrabCombat2(p1, p2)

    def turn(self):
        self.history.append([self.p1[:], self.p2[:]])

        print(self.p1, self.p2)

        p1_card = self.p1.pop(0)
        p2_card = self.p2.pop(0)
        print(p1_card, p2_card)

        if len(self.p1) >= p1_card and len(self.p2) >= p2_card:
            self.game[0] += 1
            print(f"\nNew Game {self.game[0]}\n")
            inner_game = CrabCombat2(
                self.p1[:p1_card], self.p2[:p2_card], game=self.game, history=[]
            )
            p1, p2 = inner_game.play()
            if p1:
                self.p1.extend([p1_card, p2_card])
                print("The winner is Player 1")
            elif p2:
                self.p2.extend([p2_card, p1_card])
                print("The winner is Player 2")
            else:
                raise NotImplementedError
            self.game[0] -= 1
            print(f"\nReturn to Game {self.game[0]}\n")
            return None

        elif p1_card > p2_card:
            self.p1.extend([p1_card, p2_card])
            print("The winner is Player 1")
        elif p2_card > p1_card:
            self.p2.extend([p2_card, p1_card])
            print("The winner is Player 2")
        else:
            raise NotImplementedError

        print(self.p1, self.p2)
        print()
        time.sleep(0.1)

    def play(self) -> int:
        while True:
            if [self.p1, self.p2] in self.history:
                return True, False
            self.turn()
            if self.p1 == [] or self.p2 == []:
                break

        return self.p1 == self.winner, self.p2 == self.winner

    @property
    def winner(self) -> List[int]:
        return self.p1 if self.p1 else self.p2

    @property
    def score(self) -> int:
        return sum(
            pos * card for pos, card in enumerate(reversed(self.winner), start=1)
        )


crab2 = CrabCombat2.from_string(TXT)
crab2.play()
assert crab2.score == 291


crab2 = CrabCombat2.from_string(txt)
crab2.play()
crab2.score