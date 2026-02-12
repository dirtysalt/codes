#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = [0] * 64
        INF = 1 << 63
        ans = INF
        j, acc = 0, 0

        for i in range(len(nums)):
            acc |= nums[i]

            for b in range(64):
                if nums[i] & (1 << b):
                    cnt[b] += 1

            while acc >= k and j <= i:
                sz = (i - j + 1)
                ans = min(ans, sz)
                # print(j, i, acc)

                for b in range(64):
                    if nums[j] & (1 << b):
                        cnt[b] -= 1
                        if cnt[b] == 0:
                            acc &= ~(1 << b)
                j += 1


        if ans == INF:
            ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3], 2, 1),
    ([2, 1, 8], 10, 3),
    ([1, 2, ], 0, 1),
    ([32, 2, 24, 1], 35, 3),
    ([6, 21, 20], 19, 1)
]

aatest_helper.run_test_cases(Solution().minimumSubarrayLength, cases)

if __name__ == '__main__':
    pass
