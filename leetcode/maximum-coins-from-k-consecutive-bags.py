#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins = [(l, r, c) for (l, r, c) in coins]
        coins.sort()
        starts = []
        for l, r, c in coins:
            starts.append(l - k + 1)
            starts.append(l)
            starts.append(r - k + 1)
            starts.append(r)
        starts = [x for x in starts if x >= coins[0][0]]
        starts = list(set(starts))
        starts.sort()

        # print(starts)
        ans = res = 0
        i, j = 0, 0
        l, r = coins[0][0], coins[0][0]
        for p in starts:
            while l < p and i < len(coins):
                if p <= coins[i][1]:
                    res -= (p - l) * coins[i][2]
                    l = p
                else:
                    res -= (coins[i][1] - l + 1) * coins[i][2]
                    i += 1
                    if i < len(coins):
                        l = coins[i][0]

            pk = p + k
            while r < pk and j < len(coins):
                if pk <= coins[j][1]:
                    res += (pk - r) * coins[j][2]
                    r = pk
                else:
                    res += (coins[j][1] - r + 1) * coins[j][2]
                    j += 1
                    if j < len(coins):
                        r = coins[j][0]

            # print(p, res)
            ans = max(ans, res)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[8, 10, 1], [1, 3, 2], [5, 6, 4]], 4, 10),
    ([[1, 10, 3]], 2, 6),
]

aatest_helper.run_test_cases(Solution().maximumCoins, cases)

if __name__ == '__main__':
    pass
