#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import aatest_helper


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = set()

    def add(self, key: int) -> None:
        self.lookup.add(key)

    def remove(self, key: int) -> None:
        if key in self.lookup:
            self.lookup.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.lookup


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

cases = [
    (["MyHashSet", "add", "remove", "add", "remove", "remove", "add", "add", "add", "add", "remove"],
     [[], [9], [19], [14], [19], [9], [0], [3], [4], [0], [9]],
     [None, None, None, None, None, None, None, None, None, None, None])
]
aatest_helper.run_simulation_cases(MyHashSet, cases)
