#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        class Node:
            def __init__(self):
                self.child = [None, None]
                self.minNum = -1

        root = None
        maxValue = max(nums)
        for x, _ in queries:
            maxValue = max(maxValue, x)
        maxBits = 1
        while (1 << maxBits) < maxValue:
            maxBits += 1

        def build(root, x, bit):
            if root is None:
                n = Node()
                n.minNum = x
                root = n

            if bit == -1:
                return root

            b = (x >> bit) & 0x1
            root.child[b] = build(root.child[b], x, bit - 1)
            root.minNum = min(root.minNum, root.child[b].minNum)
            return root

        for x in nums:
            root = build(root, x, maxBits - 1)

        # print(root.minNum)
        ans = []

        def test(root, x, m):
            if root.minNum > m: return -1
            res = 0
            for i in reversed(range(maxBits)):
                b = (x >> i) & 0x1
                if root.child[1 - b] and root.child[1 - b].minNum <= m:
                    res |= (1 << i)
                    root = root.child[1 - b]
                else:
                    root = root.child[b]
            return res

        for x, m in queries:
            res = test(root, x, m)
            ans.append(res)
        return ans


cases = [
    ([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]], [3, 3, 7]),
    ([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]], [15, -1, 5]),
    ([5, 2, 4, 6, 6, 3], [[6,3]], [5]),

]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximizeXor, cases)
