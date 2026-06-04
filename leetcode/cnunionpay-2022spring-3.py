#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def maxInvestment(self, product: List[int], limit: int) -> int:

        def test(t):
            cnt = 0
            for p in product:
                if t <= p:
                    cnt += (p - t + 1)
            return cnt

        s, e = 0, max(product)
        while s <= e:
            m = (s + e) // 2
            if test(m) <= limit:
                e = m - 1
            else:
                s = m + 1

        MOD = 10 ** 9 + 7
        t = s
        ans = 0
        cnt = 0
        import heapq
        hp = []
        for p in product:
            if t <= p:
                cnt += (p - t + 1)
                ans += ((p + t) * (p - t + 1)) // 2
                heapq.heappush(hp, -(t - 1))
            else:
                heapq.heappush(hp, -p)

        # print(ans, hp, cnt)
        while cnt < limit and hp:
            x = -heapq.heappop(hp)
            if x > 0:
                cnt += 1
                ans += x
                heapq.heappush(hp, -(x - 1))
        return ans % MOD

true, false, null = True, False, None
cases = [
    ([4, 5, 3], 8, 26),
    ([2, 1, 3], 20, 10),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxInvestment, cases)

if __name__ == '__main__':
    pass
