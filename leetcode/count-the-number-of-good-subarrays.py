#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        from collections import Counter
        cnt = Counter()
        n = len(nums)

        def C2(n):
            if n <= 1: return 0
            return n * (n - 1) // 2

        def update(i, d):
            c = 0
            c -= C2(cnt[nums[i]])
            cnt[nums[i]] += d
            c += C2(cnt[nums[i]])
            return c

        j, c = 0, 0
        ans = 0
        for i in range(n):
            while c < k and j < n:
                c += update(j, 1)
                j += 1
                if c >= k:
                    break
            if c >= k:
                ans += (n - j + 1)
            c += update(i, -1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 1, 1, 1, 1], 10, 1),
    ([3, 1, 4, 3, 2, 2, 4], 2, 4),
]

aatest_helper.run_test_cases(Solution().countGood, cases)

if __name__ == '__main__':
    pass
