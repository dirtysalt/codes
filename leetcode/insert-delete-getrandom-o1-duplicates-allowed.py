#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random
from collections import defaultdict


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.value_indices = defaultdict(list)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        idx = list(self.values)
        indices = self.value_indices[val]
        result = len(indices) == 0
        idx2 = len(indices)

        self.value_indices[val].append(idx)
        self.values.append((val, idx2))
        return result

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        indices = self.value_indices[val]
        if not indices:
            return False
        idx = indices[-1]
        indices.pop()
        if idx != len(self.values) - 1:
            self.values[-1], self.values[idx] = self.values[idx], self.values[-1]
            x = self.value[idx]
            self.value_indices[x[0]][x[1]] = idx
        self.values.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if not self.values:
            return None
        pos = random.randint(0, len(self.values) - 1)
        return self.values[pos][0]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
