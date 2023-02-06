#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq
        hp = [-x for x in gifts]
        heapq.heapify(hp)

        for _ in range(k):
            x = heapq.heappop(hp)
            x = -x
            left = int(x ** 0.5)
            heapq.heappush(hp, -left)

        ans = -sum(hp)
        return ans


if __name__ == '__main__':
    pass
