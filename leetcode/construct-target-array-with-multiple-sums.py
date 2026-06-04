#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        hp = []
        s = 0
        for x in target:
            hp.append(-x)
            s += x
        import heapq
        heapq.heapify(hp)

        while hp[0] != -1:
            x = -hp[0]
            rest = s - x
            if x <= rest or rest == 0:
                return False

            x %= rest
            if x == 0:
                x = rest
            s = x + rest
            heapq.heappushpop(hp, -x)
        return True
