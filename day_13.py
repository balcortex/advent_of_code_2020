from __future__ import annotations
from typing import Sequence


class BusSchedule:
    def __init__(self, ts: int, buses: Sequence[int]):
        self.ts = ts
        self.buses = buses

    @property
    def id_minutes(self) -> int:
        ts = self.ts

        while True:
            for bus in self.buses:
                if ts % bus == 0:
                    return (ts - self.ts) * bus
            ts += 1

    @classmethod
    def parse(cls, s: str) -> BusSchedule:
        s_ = s.split("\n")
        ts = int(s_[0])
        buses = [int(bus) for bus in s_[1].split(",") if bus.isdigit()]
        return cls(ts, buses)


bussc = BusSchedule.parse("939\n7,13,x,x,59,x,31,19")
assert bussc.id_minutes == 295

with open("day_13_input.txt") as f:
    bussc = BusSchedule.parse(f.read())
    print(bussc.id_minutes)


class BusSchedule2:
    def __init__(self, ts: int, buses: Sequence[int]):
        self.ts = ts
        self.buses = buses

    # @property
    # def earliest_ts(self) -> int:
    #     ts = self.ts
    #     max0 = max(self.buses)
    #     max1 = sorted(self.buses)[1]

    #     while True:
    #         if ts % 1000000 == 0:
    #             print(ts)
    #         if ts % max0 == 0:
    #             ts -= self.buses.index(max0)
    #             departed = (
    #                 (ts + idx) % bus == 0
    #                 for (idx, bus) in enumerate(self.buses)
    #                 if not bus == 1
    #             )

    #             if all(departed):
    #                 return ts
    #             ts += self.buses.index(max0)

    #             ts += max0

    #         else:
    #             ts += 1

    # @property
    # def earliest_ts(self) -> int:
    #     ts = self.ts
    #     buses_sort = sorted(
    #         [(bus, i) for (i, bus) in enumerate(self.buses)], reverse=True
    #     )
    #     bus_max_1 = buses_sort[0][0]
    #     bus_max_2 = buses_sort[1][0]
    #     bus_idx_1 = buses_sort[0][1]
    #     bus_idx_2 = buses_sort[1][1]
    #     idx_dif = bus_idx_2 - bus_idx_1
    #     print(f"{bus_max_1=}")
    #     print(f"{bus_max_2=}")
    #     print(f"{bus_idx_1=}")
    #     print(f"{bus_idx_2=}")
    #     print(f"{idx_dif=}")

    #     while True:
    #         if ts % 1000000 == 0:
    #             print(ts)

    #         if ts % bus_max_1 == 0 and (ts + idx_dif) % bus_max_2 == 0:
    #             ts -= bus_idx_1
    #             departed = (
    #                 (ts + idx) % bus == 0
    #                 for (idx, bus) in enumerate(self.buses)
    #                 if not bus == 1
    #             )

    #             if all(departed):
    #                 return ts
    #             ts += bus_idx_1

    #             ts += bus_max_1 * bus_max_2

    #         else:
    #             ts += 1

    @property
    def earliest_ts(self) -> int:
        ts = self.ts
        buses_sort = sorted(
            [(bus, i) for (i, bus) in enumerate(self.buses)], reverse=True
        )
        bus_max_1 = buses_sort[0][0]
        bus_max_2 = buses_sort[1][0]
        bus_max_3 = buses_sort[2][0]
        bus_max_4 = buses_sort[3][0]
        bus_idx_1 = buses_sort[0][1]
        bus_idx_2 = buses_sort[1][1]
        bus_idx_3 = buses_sort[2][1]
        bus_idx_4 = buses_sort[3][1]

        while True:
            if ts % 1000000 == 0:
                print(f"{404517869995362 - ts}")

            if (
                (ts + bus_idx_1) % bus_max_1 == 0
                and (ts + bus_idx_2) % bus_max_2 == 0
                and (ts + bus_idx_3) % bus_max_3 == 0
            ):
                departed = (
                    (ts + idx) % bus == 0
                    for (idx, bus) in enumerate(self.buses)
                    if not bus == 1
                )

                if all(departed):
                    return ts

                ts += bus_max_1 * bus_max_2 * bus_max_3

            else:
                ts += 1

    @classmethod
    def parse(cls, s: str) -> BusSchedule:
        s_ = s.split("\n")
        ts = int(s_[0])
        buses = [int(bus) if bus.isdigit() else 1 for bus in s_[1].split(",")]
        return cls(ts, buses)


bussc2 = BusSchedule2.parse("939\n7,13,x,x,59,x,31,19")
assert bussc2.earliest_ts == 1068781
print("Done")
bussc2 = BusSchedule2.parse("939\n17,x,13,19")
assert bussc2.earliest_ts == 3417
print("Done")
bussc2 = BusSchedule2.parse("939\n67,x,7,59,61")
assert bussc2.earliest_ts == 779210
print("Done")

with open("day_13_input.txt") as f:
    bussc2_ = BusSchedule2.parse(f.read())
    print(bussc2_.earliest_ts)