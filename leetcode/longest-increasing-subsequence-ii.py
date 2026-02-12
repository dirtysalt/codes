#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class RangeMaxTree:
    def __init__(self, sz):
        n = 1
        while n < sz:
            n = n * 2
        self.n = n
        self.sz = sz
        self.values = [0] * (2 * n)

    def update(self, idx, x):
        off = self.n + idx
        self.values[off] = x
        while off > 1:
            p = off // 2
            self.values[p] = max(self.values[2 * p], self.values[2 * p + 1])
            off = p

    def max(self):
        return self.values[1]

    def current(self, idx):
        return self.values[idx + self.n]

    def query(self, a, b):
        def search(p, off, size):
            x, y = off, off + size - 1
            if x >= a and y <= b:
                return self.values[p]
            if x > b or y < a:
                return 0

            half = size // 2
            vx = search(2 * p, off, half)
            vy = search(2 * p + 1, off + half, half)
            return max(vx, vy)

        return search(1, 0, self.n)


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        size = max(nums) + 1
        tree = RangeMaxTree(size)
        ans = 0
        for x in nums:
            a, b = max(x - k, 0), max(x - 1, 0)
            tail = tree.query(a, b)
            now = tree.current(x)
            v = max(now, tail + 1)
            tree.update(x, v)
            ans = max(ans, v)
        return ans


true, false, null = True, False, None
cases = [
    ([2, 4], 3, 2),
    ([4, 2, 1, 4, 3, 4, 5, 8, 15], 3, 5),
    ([7, 4, 5, 1, 8, 12, 4, 7], 5, 4),
    ([1, 5], 1, 1),
    ([1, 100, 500, 100000, 100000], 100000, 4),
    ([1, 3, 3, 4], 1, 2),
    ([1, 2, 3, 5, 2], 1, 3),
    ([10, 3, 20, 2, 16, 12], 4, 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().lengthOfLIS, cases)

if __name__ == '__main__':
    pass
