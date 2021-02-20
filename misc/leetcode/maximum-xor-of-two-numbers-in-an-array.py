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
            v1, idx1 = t.query(v)
            # print('#{} = {}, #{} = {}'.format(idx, v, idx1, v1))
            res = max(res, v ^ v1)
        return res


if __name__ == '__main__':
    s = Solution()
    print((s.findMaximumXOR([3, 10, 5, 25, 2, 8])))
