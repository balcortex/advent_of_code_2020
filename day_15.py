from typing import Sequence


class Recitation:
    def __init__(self, inpts: Sequence[int]):
        self.numbers = {key: [val + 1, 0] for val, key in enumerate(inpts)}
        self.last_key = inpts[-1]
        self.next_idx = len(inpts)

    def turn(self) -> int:
        if self.numbers[self.last_key][1] == 0:
            self.numbers[self.last_key][1] = self.next_idx
            self.last_key = 0
            self.next_idx += 1

        else:
            self.numbers[self.last_key][1] = self.next_idx
            self.last_key = (
                self.numbers[self.last_key][1] - self.numbers[self.last_key][1]
            )
            self.next_idx += 1


rec = Recitation([0, 3, 6])
print(rec.numbers)
rec.turn()
print(f"{rec.numbers=}")
print(f"{rec.last_key=}")
print(f"{rec.next_idx=}")
