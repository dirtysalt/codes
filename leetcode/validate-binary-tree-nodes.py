#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ind = [0] * n
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l != -1 and r != -1 and l == r:
                return False
            if l != -1:
                ind[l] += 1
            if r != -1:
                ind[r] += 1

        src = None
        for i in range(n):
            if ind[i] == 0:
                if src is not None:
                    return False
                src = i
        if src is None:
            return False

        from collections import deque
        visit = [0] * n
        dq = deque()
        dq.append(src)
        visit[src] = 1
        while dq:
            x = dq.popleft()
            l, r = leftChild[x], rightChild[x]
            for y in (l, r):
                if y == -1: continue
                if visit[y]: return False
                visit[y] = 1
                dq.append(y)

        if sum(visit) != n:
            return False
        return True


cases = [
    (4, [1, -1, 3, -1], [2, -1, -1, -1], True),
    (6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1], False),
    (2, [1, 0], [-1, -1], False)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().validateBinaryTreeNodes, cases)
