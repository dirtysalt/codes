#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        good_numbers = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        coprimes = set()

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        for x in range(1, 31):
            for y in range(1, 31):
                if gcd(x, y) == 1:
                    coprimes.add((x, y))

        cnt = [0] * 31
        for x in nums:
            cnt[x] += 1

        counters = []
        for p in primes:
            tmp = []
            for x in good_numbers:
                if x % p == 0 and cnt[x] != 0:
                    tmp.append((x, cnt[x]))
                    cnt[x] = 0  # not select anymore
            counters.append(tmp)

        def dfs(k, select):
            if k == len(primes):
                return 1

            res = dfs(k + 1, select)
            for x, c in counters[k]:
                ok = True
                for p in select:
                    if (x, p) not in coprimes:
                        ok = False
                        break

                if ok:
                    select.append(x)
                    res += c * dfs(k + 1, select)
                    select.pop()

            return res

        # print(counters)

        # including empty set.
        ans = dfs(0, []) - 1
        ans *= (1 << cnt[1])

        MOD = 10 ** 9 + 7
        return ans % MOD


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 4], 6),
    ([4, 2, 3, 15], 5),
    ([18, 28, 2, 17, 29, 30, 15, 9, 12], 19)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfGoodSubsets, cases)

if __name__ == '__main__':
    pass
