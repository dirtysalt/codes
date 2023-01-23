#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class NumberContainers:

    def __init__(self):
        from sortedcontainers import SortedSet
        from collections import defaultdict
        self.dd = defaultdict(SortedSet)
        self.content = {}

    def change(self, index: int, number: int) -> None:
        if index in self.content:
            old = self.content[index]
            self.dd[old].remove(index)

        self.content[index] = number
        self.dd[number].add(index)

    def find(self, number: int) -> int:
        ss = self.dd.get(number)
        if ss is not None and ss:
            return ss[0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

if __name__ == '__main__':
    pass
