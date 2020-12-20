#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        from collections import Counter
        cnt = Counter(inventory)
        hp = []
        for k in cnt.keys():
            hp.append(-k)
        import heapq
        heapq.heapify(hp)

        ans = 0
        while orders:
            k = -heapq.heappop(hp)
            v = cnt[k]
            k2 = 0
            if hp:
                k2 = -heapq.heappop(hp)

            # takes `rnd` rounds
            # values = k * v + (k-1) * v + ... (k-rnd+1) * v
            # items = rnd * v
            # rem = orders - rnd * v
            # and rem values = rem * (k-rnd)
            rnd = orders // v
            value = 0
            if rnd <= (k - k2):
                rem = orders - rnd * v
                value += (k - rnd) * rem
                orders = 0
            else:
                rnd = k - k2
                orders -= rnd * v
                cnt[k2] += v
                heapq.heappush(hp, -k2)
            value += (2 * k - rnd + 1) * rnd * v // 2
            # print(k, k2, v, orders, value)
            ans += value

        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans


cases = [
    ([2, 5], 4, 14),
    ([3, 5], 6, 19),
    ([2, 8, 4, 10, 6], 20, 110),
    ([1000000000], 1000000000, 21),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProfit, cases)
