#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class SeatManager:

    def __init__(self, n: int):
        import heapq
        self.hp = list(range(n))
        heapq.heapify(self.hp)

    def reserve(self) -> int:
        x = heapq.heappop(self.hp)
        return x + 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.hp, seatNumber - 1)

if __name__ == '__main__':
    pass
