#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        import heapq
        hp = nums.copy()
        heapq.heapify(hp)
        for _ in range(k):
            x = heapq.heappop(hp)
            heapq.heappush(hp, x + 1)

        ans = 1
        MOD = 10 ** 9 + 7
        for x in hp:
            ans = ans * x
            ans %= MOD
        return ans


if __name__ == '__main__':
    pass
