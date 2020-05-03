#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minJump(self, jump: List[int]) -> int:
        n = len(jump)
        depth = [0] * n

        from collections import deque
        dq = deque()
        dq.append(0)
        max_left = 0
        ans = 0

        while dq:
            x = dq.popleft()
            y = x + jump[x]
            if y >= n:
                ans = depth[x] + 1
                break

            if not depth[y]:
                depth[y] = depth[x] + 1
                dq.append(y)

            for y in range(max_left + 1, x):
                if not depth[y]:
                    depth[y] = depth[x] + 1
                    dq.append(y)
            max_left = max(max_left, x)

        return ans
