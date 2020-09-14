#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Heap:
    def __init__(self, max_size, cmpfn):
        base = 1
        while base < max_size:
            base *= 2
        self.items = [None] * (2 * base)
        self.base = base
        self.cmpfn = cmpfn

    def fix(self, idx):
        while idx > 1:
            p = idx // 2
            l, r = 2 * p, 2 * p + 1
            if self.items[l] is None and self.items[r] is None:
                self.items[p] = None
            elif self.items[l] is None or self.items[r] is None:
                self.items[p] = self.items[l] or self.items[r]
            else:
                if self.cmpfn(self.items[l], self.items[r]):
                    self.items[p] = self.items[l]
                else:
                    self.items[p] = self.items[r]
            idx = p

    def set_index(self, index, v):
        self.items[self.base + index] = v
        self.fix(self.base + index)

    def top(self):
        return self.items[1]


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        tmp = [(x, idx) for (idx, x) in enumerate(nums[:k])]
        lhp = Heap(k, cmpfn=lambda x, y: x[0] > y[0])
        rhp = Heap(k, cmpfn=lambda x, y: x[0] < y[0])

        tmp.sort()
        indices = {}
        lsz, rsz = 0, 0

        for i in range(0, (k + 1) // 2):
            lhp.set_index(i, tmp[i])
            indices[tmp[i][1]] = (0, i)
        for i in range((k + 1) // 2, k):
            rhp.set_index(i, tmp[i])
            indices[tmp[i][1]] = (1, i)

        def median():
            # print(lhp.top(), rhp.top())
            if k % 2 == 0:
                return (lhp.top()[0] + rhp.top()[0]) * 0.5
            return lhp.top()[0]

        ans = []
        ans.append(median())

        # print(indices)
        for i in range(k, len(nums)):
            # remove i-k and add i
            (lr, hidx) = indices[i - k]
            if lr == 0:
                lhp.set_index(hidx, (nums[i], i))
                indices[i] = (0, hidx)
            else:
                rhp.set_index(hidx, (nums[i], i))
                indices[i] = (1, hidx)

            # 但是此时 lhp.top() 可能会 > rhp.top()
            # 如果是这种情况的话，需要交换顶层两个元素
            if rhp.top() and lhp.top()[0] > rhp.top()[0]:
                (rv, ridx) = rhp.top()
                assert indices[ridx][0] == 1
                hridx = indices[ridx][1]
                (lv, lidx) = lhp.top()
                assert indices[lidx][0] == 0
                hlidx = indices[lidx][1]

                lhp.set_index(hlidx, (rv, ridx))
                indices[ridx] = (0, hlidx)
                rhp.set_index(hridx, (lv, lidx))
                indices[lidx] = (1, hridx)

            # print(indices)
            # print(i, median())
            ans.append(median())
        return ans


cases = [
    ([1, 2], 1, [1, 2]),
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [1, -1, -1, 3, 5, 6]),
    ([-1, -3, 5, 3], 3, [-1, 3]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().medianSlidingWindow, cases)
