#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        hp = [-x for x in piles]
        heapq.heapify(hp)

        for _ in range(k):
            x = -heapq.heappop(hp)
            d = x // 2
            x = x - d
            heapq.heappush(hp, -x)

        ans = 0
        for x in hp:
            ans -= x
        return ans


if __name__ == '__main__':
    pass
