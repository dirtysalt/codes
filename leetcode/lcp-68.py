#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        from collections import Counter
        C = Counter()
        j, n = 0, len(flowers)
        ans = 0
        for i in range(n):
            x = flowers[i]
            C[x] += 1
            if C[x] > cnt:
                while C[x] > cnt:
                    C[flowers[j]] -= 1
                    j += 1
            ans += (i - j + 1)

        MOD = 10 ** 9 + 7
        return ans % MOD


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 2], 1, 8),
    ([5, 3, 3, 3], 2, 8),
    ([98495, 98495, 99801, 34717, 34717, 99801, 98495, 99801, 99801, 98495], 2, 39),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().beautifulBouquet, cases)

if __name__ == '__main__':
    pass
