#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Tree:
    def __init__(self, op='', val=None):
        self.op = op
        self.val = val
        self.left = None
        self.right = None

    def _cost(self):
        if self.op == '':
            if self.val == 1:
                return 1, 1, 0
            return 0, 0, 1

        lv, l0, l1 = self.left.cost()
        rv, r0, r1 = self.right.cost()

        if self.op == '&':
            old = lv & rv
            a = min(l0 + r0, l0 + r1, r0 + l1)  # 0
            b = l1 + r1  # 1
            # or change to |
            c = l0 + r0 + 1  # 0
            d = min(l0 + r1, l1 + r0, l1 + r1) + 1  # 1
            return old, min(a, c), min(b, d)

        if self.op == '|':
            old = lv | rv
            a = l0 + r0
            b = min(l1 + r0, l0 + r1, l1 + r1)
            # or change to &
            c = min(l0 + r0, l0 + r1, l1 + r0) + 1
            d = l1 + r1 + 1
            return old, min(a, c), min(b, d)

    def cost(self):
        c = self._cost()
        # print(self, c)
        return c

    def __str__(self):
        if self.op == '':
            return '%d' % (self.val)
        return '(op = %s, L = %s, R = %s)' % (self.op, self.left, self.right)


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:

        def buildTree(offset, expr):
            st = []
            end = len(expr)
            i = offset

            while i < len(expr):
                if expr[i] == '(':
                    i, t = buildTree(i + 1, expr)
                    st.append(t)
                    continue

                if expr[i] == ')':
                    end = i + 1
                    break

                if expr[i] in '&|':
                    st.append(Tree(op=expr[i]))

                elif expr[i] in '01':
                    st.append(Tree(op='', val=int(expr[i])))
                i += 1

            # use right eval order.
            st = st[::-1]
            right = st.pop()
            while st:
                op = st.pop()
                left = st.pop()
                op.left = left
                op.right = right
                right = op
            return end, right

        end, right = buildTree(0, expression)
        assert end == len(expression)
        # print(right)
        old, a, b = right.cost()
        if old == 0:
            return b
        return a


true, false, null = True, False, None
cases = [
    ("1&(0|1)", 1),
    ("(0&0)&(0&0&0)", 3),
    ("(0|(1|0&1))", 1),
    ("1|1|(0&0)&1", 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperationsToFlip, cases)

if __name__ == '__main__':
    pass
