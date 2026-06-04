#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class SmallestInfiniteSet:

    def __init__(self):
        # self.ss = SortedSet()
        self.ss = set()

    def popSmallest(self) -> int:
        val = 1
        while val in self.ss:
            val += 1
        self.ss.add(val)
        return val

    def addBack(self, num: int) -> None:
        if num in self.ss:
            self.ss.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

if __name__ == '__main__':
    pass
