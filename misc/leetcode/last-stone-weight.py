#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for x in stones:
            hp.append(-x)
        import heapq
        heapq.heapify(hp)

        while len(hp) > 1:
            x = -heapq.heappop(hp)
            y = -heapq.heappop(hp)
            if x == y:
                continue
            assert x > y
            heapq.heappush(hp, -(x - y))
        ans = 0
        if hp:
            ans = -hp[0]
        return ans
