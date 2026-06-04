#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = []
        for i in range(n):
            diff.append(abs(nums1[i] - nums2[i]))

        # 如果可以全部调整完成
        if sum(diff) <= (k1 + k2):
            return 0

        diff.sort(reverse=True)
        tt = 0
        index = 0
        k = k1 + k2
        # 如果前面index个元素全部下降到diff[index]的话，那么会超过k
        # 说明我们最多调整前面index个元素
        while index < n:
            if (tt - (diff[index] * index)) > k:
                break
            tt += diff[index]
            index += 1

        # 前面index个元素调整的话，至少可以调整到
        # base = floor((tt - k) / index) = (tt - k + index - 1) // index
        base = (tt - k + index - 1) // index
        for i in range(index):
            delta = diff[i] - base
            diff[i] -= delta
            k -= delta
        for i in range(index):
            if k > 0:
                diff[i] -= 1
                k -= 1

        ans = sum((x * x for x in diff))
        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 4], [2, 10, 20, 19], 0, 0, 579),
    ([1, 4, 10, 12], [5, 8, 6, 9], 1, 1, 43),
    ([1, 4, 10, 12], [5, 8, 6, 9], 10, 5, 0),
    ([7, 11, 4, 19, 11, 5, 6, 1, 8], [4, 7, 6, 16, 12, 9, 10, 2, 10], 3, 6, 27),
    ([11, 12, 13, 14, 15], [13, 16, 16, 12, 14], 3, 6, 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSumSquareDiff, cases)

if __name__ == '__main__':
    pass
