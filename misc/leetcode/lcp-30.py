#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0: return -1

        import heapq
        hp = []
        now = 1
        ans = 0
        for x in nums:
            if x < 0:
                heapq.heappush(hp, x)
            now += x
            if now <= 0:
                while hp and now <= 0:
                    t = heapq.heappop(hp)
                    now -= t
                    ans += 1

        return ans

cases = [
    ([100,100,100,-250,-60,-140,-50,-50,100,150], 1),
    ([-200,-300,400,0], -1),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().magicTower, cases)


if __name__ == '__main__':
    pass
