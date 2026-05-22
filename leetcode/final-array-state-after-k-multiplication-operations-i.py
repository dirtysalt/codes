#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        import heapq
        q = []
        for i in range(len(nums)):
            q.append((nums[i], i))
        heapq.heapify(q)

        ans = [0] * len(nums)
        for _ in range(k):
            (x, idx) = heapq.heappop(q)
            heapq.heappush(q, (x * multiplier, idx))

        for (x, idx) in q:
            ans[idx] = x
        return ans


if __name__ == '__main__':
    pass
