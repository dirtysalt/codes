#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        class Node:
            def __init__(self):
                self.value = 0
                self.mask = 0
                self.count = 0
            def __repr__(self):
                return '({}, {}, {})'.format(self.value, self.mask, self.count)

        msb = 1
        for x in nums:
            for i in reversed(range(1, 17)):
                if (x & (1 << i)):
                    msb = max(msb, i)
                    break
        N = 1 << (msb + 1)


        nodes = [Node() for _ in range(2 * N)]
        for x in nums:
            node = nodes[N + x]
            node.count += 1

        for i in range(N):
            node = nodes[N + i]
            node.value = i
            node.mask = 0

        for i in reversed(range(1, N)):
            c0 = 2 * i
            c1 = 2 * i + 1
            node = nodes[i]
            node.value = nodes[c0].value
            node.mask = nodes[c0].mask + 1
            assert(nodes[c0].mask == nodes[c1].mask)
            node.count = nodes[c0].count + nodes[c1].count

        def query(base, thres, idx):
            n = nodes[idx]
            mask  = (1 << n.mask) - 1
            tmax = (n.value ^ base) | mask
            tmin = (n.value ^ base) & (~mask)
            if tmax <= thres:
                return n.count
            if tmin > thres:
                return 0
            if n.mask == 0 or n.count == 0:
                return 0
            c0 = query(base, thres, idx * 2)
            c1 = query(base, thres, idx * 2 + 1)
            return c0 + c1


        n = len(nums)
        ans = 0
        for i in range(n):
            base = nums[i]
            c1 = query(base, high, 1)
            c0 = query(base, low - 1, 1)
            d = c1 - c0
            if low <= (base ^ base) <= high:
                d -= 1
            ans += d

        ans = ans // 2
        return ans

cases = [
([1,4,2,7], 2,6,6),
([9,8,4,2,1], 5,14,8),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().countPairs, cases)



if __name__ == '__main__':
    pass
