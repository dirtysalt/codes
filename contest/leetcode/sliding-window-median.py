#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        tmp = [(x, idx) for (idx, x) in enumerate(nums[:k])]
        tmp.sort()
        indices = {}
        for pos, (x, idx) in enumerate(tmp):
            indices[idx] = pos

        def median(xs):
            n = len(xs)
            if n % 2 == 0:
                return (xs[n // 2 - 1][0] + xs[n // 2][0]) * 0.5
            return xs[n // 2][0]

        def swap(a, b):
            x, i = tmp[a]
            y, j = tmp[b]
            tmp[a] = y, j
            indices[j] = a
            tmp[b] = x, i
            indices[i] = b

        ans = []
        ans.append(median(tmp))

        # O(n^2)
        for i in range(k, len(nums)):
            # add nums[i] and remove nums[i-k]
            tp = indices[i - k]
            tmp[tp] = (nums[i], i)
            indices[i] = tp
            # print('>>>>', tmp, indices)

            # run bubble sort, fix tmp and indices
            j = tp
            while (j + 1) < len(tmp) and tmp[j][0] > tmp[j + 1][0]:
                swap(j, j + 1)
                j = j + 1
            j = tp
            while (j - 1) >= 0 and tmp[j][0] < tmp[j - 1][0]:
                swap(j, j - 1)
                j = j - 1

            # print('<<<<<', tmp, indices)

            ans.append(median(tmp))

        return ans



cases = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [1, -1, -1, 3, 5, 6])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().medianSlidingWindow, cases)
