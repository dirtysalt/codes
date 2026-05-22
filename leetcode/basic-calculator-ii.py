#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# note(yan): 这个程序还是比较adhoc的，没有办法处理多个优先级

class Solution:
    def calculate(self, s: str) -> int:
        values = []
        ops = []

        import string

        def reduce_mul_div():
            while ops:
                if ops[-1] not in "*/":
                    break
                op = ops.pop()
                v1 = values.pop()
                v2 = values.pop()
                if op == '*':
                    v = v1 * v2
                elif op == '/':
                    v = v2 // v1
                else:
                    raise RuntimeError('unexpected op = {}'.format(op))
                values.append(v)

        def reduce_add_sub():
            res = values[0]
            for i in range(len(ops)):
                op = ops[i]
                if op == '+':
                    res += values[i + 1]
                else:
                    res -= values[i + 1]
            return res

        res = 0
        for c in s:
            if c == ' ':
                continue

            elif c in string.digits:
                res = res * 10 + ord(c) - ord('0')

            else:
                values.append(res)
                reduce_mul_div()
                res = 0
                ops.append(c)

        values.append(res)
        reduce_mul_div()
        ans = reduce_add_sub()
        return ans


import aatest_helper

cases = [
    ("3+2*2", 7),
    (" 3+5 / 2 ", 5),
    (" 3/2 ", 1),
    ('1-1+1', 1)
]

aatest_helper.run_test_cases(Solution().calculate, cases)
