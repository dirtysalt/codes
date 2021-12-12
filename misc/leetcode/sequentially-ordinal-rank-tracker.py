#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sortedcontainers import SortedList


class SORTracker:

    def __init__(self):
        self.sl = SortedList()
        self.qc = 0

    def add(self, name: str, score: int) -> None:
        self.sl.add((-score, name))

    def get(self) -> str:
        qc = self.qc
        self.qc += 1
        value = self.sl[qc]
        # print(self.sl, qc, value[1])
        return value[1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()

true, false, null = True, False, None
cases = [
    (["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"],
     [[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2],
      [], []],
     [null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]
     )
]

import aatest_helper

aatest_helper.run_simulation_cases(SORTracker, cases)

if __name__ == '__main__':
    pass
