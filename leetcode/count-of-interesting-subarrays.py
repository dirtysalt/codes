#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        from collections import Counter
        cnt = Counter()

        t = 0
        for x in nums:
            if x % modulo == k:
                t = (t + 1) % modulo
            cnt[t] += 1

        t = 0
        ans = 0
        for x in nums:
            exp = (t + k) % modulo
            ans += cnt[exp]
            if x % modulo == k:
                t = (t + 1) % modulo
            cnt[t] -= 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 2, 4], 2, 1, 3),
    ([3, 1, 9, 6], 3, 0, 2),
]

aatest_helper.run_test_cases(Solution().countInterestingSubarrays, cases)

if __name__ == '__main__':
    pass
