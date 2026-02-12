#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        import heapq
        hp = []
        for i in range(len(nums)):
            hp.append((nums[i], i))
        heapq.heapify(hp)
        mark = set()

        ans = []
        total = sum(nums)
        for idx, k in queries:
            if idx not in mark:
                total -= nums[idx]
                mark.add(idx)

            while k and hp:
                (x, idx) = heapq.heappop(hp)
                if idx in mark: continue
                mark.add(idx)
                total -= nums[idx]
                k -= 1

            ans.append(total)
        return ans


if __name__ == '__main__':
    pass
