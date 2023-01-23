#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        dp = {}
        inf = 1 << 30

        def run(idx, depth):
            if depth < 0:
                return inf, [""]

            if idx == -1:
                return 0 if depth == 0 else inf, [""]

            key = '{}.{}'.format(idx, depth)
            if key in dp:
                return dp[key]

            if s[idx] == '(':
                # search run(idx-1, depth-1) not dropping
                # or search run(idx-1, depth) by droppping me
                x0, y0 = run(idx - 1, depth - 1)
                x1, y1 = run(idx - 1, depth)
                x1 += 1
                if x0 < x1:
                    res = [x + s[idx] for x in y0]
                    cost = x0
                elif x0 > x1:
                    res = y1
                    cost = x1
                else:
                    res = [x + s[idx] for x in y0] + y1
                    cost = x0
                pass

            elif s[idx] == ')':
                # search run(idx-1, depth+1) not dropping
                # or search run(idx-1, depth) by dropping me

                x0, y0 = run(idx - 1, depth + 1)
                x1, y1 = run(idx - 1, depth)
                x1 += 1

                if x0 < x1:
                    res = [x + s[idx] for x in y0]
                    cost = x0
                elif x0 > x1:
                    res = y1
                    cost = x1
                else:
                    res = [x + s[idx] for x in y0] + y1
                    cost = x0
                pass

            else:
                cost, res = run(idx - 1, depth)
                res = [x + s[idx] for x in res]

            dp[key] = (cost, res)
            return cost, res

        cost, res = run(idx=len(s) - 1, depth=0)
        ans = list(set(res))
        # print(cost, ans)
        return ans


cases = [
    ("()())()", ["()()()", "(())()"]),
    (")(", [""]),
    ("(a)())()", ["(a)()()", "(a())()"])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().removeInvalidParentheses, cases)
