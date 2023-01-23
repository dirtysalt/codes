#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        hp = [-x for x in nums]
        heapq.heapify(hp)
        ans = 0
        for _ in range(k):
            x = -heapq.heappop(hp)
            ans += x
            x = (x + 2) // 3
            heapq.heappush(hp, -x)
        return ans


if __name__ == '__main__':
    pass
