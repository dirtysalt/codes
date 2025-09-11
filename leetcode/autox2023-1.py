#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getLengthOfWaterfallFlow(self, num: int, block: List[int]) -> int:
        import heapq
        hp = [0] * num
        for b in block:
            x = heapq.heappop(hp)
            heapq.heappush(hp, x + b)
        return max(hp)


if __name__ == '__main__':
    pass
