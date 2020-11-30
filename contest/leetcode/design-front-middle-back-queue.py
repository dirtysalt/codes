#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class FrontMiddleBackQueue:
    def __init__(self):
        from collections import deque
        self.a = deque()
        self.b = deque()

    def adjust(self):
        if len(self.a) > len(self.b):
            x = self.a.pop()
            self.b.appendleft(x)

        if len(self.a) + 2 == len(self.b):
            x = self.b.popleft()
            self.a.append(x)

    def empty(self):
        return len(self.a) == 0 and len(self.b) == 0

    def pushFront(self, val: int) -> None:
        self.a.appendleft(val)
        self.adjust()

    def pushMiddle(self, val: int) -> None:
        self.b.appendleft(val)
        self.adjust()

    def pushBack(self, val: int) -> None:
        self.b.append(val)
        self.adjust()

    def popFront(self) -> int:
        if self.empty():
            return -1

        if self.a:
            x = self.a.popleft()
        else:
            x = self.b.popleft()

        self.adjust()
        return x

    def popMiddle(self) -> int:
        if self.empty():
            return -1

        if len(self.a) == len(self.b):
            x = self.a.pop()
        else:
            x = self.b.popleft()
        self.adjust()
        return x

    def popBack(self) -> int:
        if self.empty():
            return -1
        x = self.b.pop()
        self.adjust()
        return x


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

null = None
cases = [
    (["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle",
      "popBack", "popFront"],
     [[], [1], [2], [3], [4], [], [], [], [], []],
     [null, null, null, null, null, 1, 3, 4, 2, -1]),
]

import aatest_helper

aatest_helper.run_simulation_cases(FrontMiddleBackQueue, cases)
