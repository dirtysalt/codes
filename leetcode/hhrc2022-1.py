#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def lastMaterial(self, material: List[int]) -> int:
        import heapq
        hp = [-x for x in material]
        heapq.heapify(hp)
        while len(hp) > 1:
            x = -heapq.heappop(hp)
            y = -heapq.heappop(hp)
            if x == y: continue
            heapq.heappush(hp, -abs(x - y))
        ans = 0
        if len(hp) == 1:
            ans = -hp[0]
        return ans


if __name__ == '__main__':
    pass
