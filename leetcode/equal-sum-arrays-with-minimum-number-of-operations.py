#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        cnt = [[0] * 7 for _ in range(2)]
        A = sum(nums1)
        B = sum(nums2)
        diff = A - B
        if diff < 0:
            nums1, nums2 = nums2, nums1
            diff = -diff
        for x in nums1:
            cnt[0][x] += 1
        for x in nums2:
            cnt[1][x] += 1

        ops = []
        for i in range(1, 7):
            for j in range(1, 7):
                d = i - j
                if d == 0: continue
                if d > 0:
                    ops.append((i - j, 0, i))
                else:
                    ops.append((j - i, 1, i))
        ops.sort(key=lambda x: -x[0])
        ans = 0
        for d, idx, f in ops:
            if diff == 0: break
            x = min(diff // d, cnt[idx][f])
            cnt[idx][f] -= x
            # print(x, diff // d, cnt[idx][f], diff, idx, f, d)
            diff -= d * x
            ans += x

        if diff != 0: return -1
        return ans


cases = [
    ([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2], 3),
    ([1, 1, 1, 1, 1, 1, 1], [6], -1),
    ([6, 6], [1], 3),
    ([6], [5, 4, 1, 2, 5, 3, 2, 5, 1, 5, 6, 6, 3, 6, 1, 6], -1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperations, cases)
