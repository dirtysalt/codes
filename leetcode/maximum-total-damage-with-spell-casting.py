#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # dp[i] = (dp[i-d] + p[i] * c[i]) if ok(p[i], p[i-d])
        from collections import Counter
        cnt = Counter(power)
        keys = sorted(cnt.keys())

        n = len(keys)
        dp = [0] * n

        for i in range(n):
            base = 0
            for d in range(1, 4):
                if (i - d) < 0: break
                if keys[i] - keys[i - d] > 2:
                    base = max(base, dp[i - d])
            dp[i] = max(dp[i - 1] if i > 0 else 0, base + keys[i] * cnt[keys[i]])

        print(keys, [cnt[k] for k in keys], dp)
        return max(dp)


true, false, null = True, False, None
import aatest_helper

cases = [
    ([5, 9, 2, 10, 2, 7, 10, 9, 3, 8], 31),
    ([2, 1, 4, 3, 1, 1, 1, 5], 9),
    ([1, 1, 3, 4], 6),
    ([7, 1, 6, 6], 13),
]

aatest_helper.run_test_cases(Solution().maximumTotalDamage, cases)

if __name__ == '__main__':
    pass
