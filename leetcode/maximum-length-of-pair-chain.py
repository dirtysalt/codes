#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        ans = 0
        for i in range(len(pairs)):
            k = i
            cnt = 1
            for j in range(i+1, len(pairs)):
                if pairs[j][0] > pairs[k][1]:
                    k = j
                    cnt += 1
            ans = max(ans, cnt)
        return ans

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])

        dp = []
        for x, y in pairs:
            s, e = 0, len(dp) - 1
            while s <= e:
                m = (s + e) // 2
                if dp[m] < x:
                    s = m + 1
                else:
                    e = m - 1

            # dp[s-1] < x and dp[s] >= x
            if s == len(dp):
                dp.append(y)

        ans = len(dp)
        return ans

cases = [
    ([[1,2], [2,3], [3,4]], 2),
    ([[3,4],[2,3],[1,2]], 2),
    ([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]], 4)
]

import aatest_helper
aatest_helper.run_test_cases(Solution().findLongestChain, cases)




if __name__ == '__main__':
    pass
