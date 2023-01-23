#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def parse(expr, i):
            c = expr[i]
            if c == 't':
                return True, i+1
            elif c == 'f':
                return False, i+1
            elif c == '!':
                assert(expr[i+1] == '(')
                ret, end = parse(expr, i+2)
                assert(expr[end] == ')')
                return not ret, end + 1
            elif c == '&' or c == '|':
                if c == '&':
                    ret, op = True, lambda x,y: x and y
                elif c == '|':
                    ret, op = False, lambda x, y: x or y

                assert(expr[i+1] == '(')
                i += 2
                while True:
                    tmp, end = parse(expr, i)
                    ret = op(ret, tmp)
                    i = end + 1
                    if expr[end] == ')':
                        break
                    assert expr[end] == ','
                return ret, i
            else:
                assert False, 'unknown char: ' + c

        ret, end = parse(expression, 0)
        assert end == len(expression)
        return ret

cases = [
    ("!(f)", True),
    ("|(f,t)", True),
    ("&(t,f)", False),
    ("|(&(t,f,t),!(t))", False),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().parseBoolExpr, cases)

if __name__ == '__main__':
    pass
