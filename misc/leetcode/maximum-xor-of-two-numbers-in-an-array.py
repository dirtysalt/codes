#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Trie:
    def __init__(self):
        self.bits = [None, None]
        self.value = None
        self.index = None

    def insert(self, v, idx):
        root = self
        for p in range(31, -1, -1):
            b = (v >> p) & 0x1
            if root.bits[b] is None:
                t = Trie()
                root.bits[b] = t
            root = root.bits[b]
        root.value = v
        root.index = idx

    def query(self, v):
        root = self
        for p in range(31, -1, -1):
            b = (v >> p) & 0x1
            if root.bits[1 - b] is not None:
                root = root.bits[1 - b]
            elif root.bits[b] is not None:
                root = root.bits[b]
        return root.value, root.index


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        t = Trie()
        for (idx, v) in enumerate(nums):
            t.insert(v, idx)

        res = 0
        for (idx, v) in enumerate(nums):
            v2,_ = t.query(v)
            res = max(res, v ^ v2)
        return res


true, false, null = True, False, None
cases = [
    ([3, 10, 5, 25, 2, 8], 28),
    ([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], 127),
    ([8, 10, 2], 10)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findMaximumXOR, cases)

if __name__ == '__main__':
    pass
