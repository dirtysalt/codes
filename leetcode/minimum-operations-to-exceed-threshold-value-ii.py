#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq
        hp = nums.copy()
        heapq.heapify(hp)
        ans = 0
        while True:
            if hp[0] >= k: break
            a = heapq.heappop(hp)
            b = heapq.heappop(hp)
            c = min(a, b) * 2 + max(a, b)
            heapq.heappush(hp, c)
            ans += 1
        return ans


if __name__ == '__main__':
    pass
