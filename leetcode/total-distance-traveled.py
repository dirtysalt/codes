#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5 and additionalTank > 0:
            ans += 50;
            mainTank -= 4
            additionalTank -= 1
        ans += mainTank * 10
        return ans


if __name__ == '__main__':
    pass
