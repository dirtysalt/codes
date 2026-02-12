#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:

        dist = [-1] * 1001
        from collections import deque
        dq = deque()
        dq.append(start)
        dist[start] = 0

        ops = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x ^ y]
        while dq:
            x = dq.popleft()
            d = dist[x]
            if x == goal:
                return d

            d += 1
            for y in nums:
                for op in ops:
                    z = op(x, y)
                    if 0 <= z <= 1000:
                        if dist[z] == -1:
                            dist[z] = d
                            dq.append(z)
                    elif z == goal:
                        return d

        return -1


if __name__ == '__main__':
    pass
