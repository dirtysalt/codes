#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.v2idx = {}
        self.values = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.v2idx:
            return False
        idx = len(self.values)
        self.v2idx[val] = idx
        self.values.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.v2idx:
            return False
        idx = self.v2idx[val]
        del self.v2idx[val]
        if idx != (len(self.values) - 1):
            self.values[idx] = self.values[-1]
            self.v2idx[self.values[idx]] = idx
        self.values.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.values:
            return None
        pos = random.randint(0, len(self.values) - 1)
        return self.values[pos]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
