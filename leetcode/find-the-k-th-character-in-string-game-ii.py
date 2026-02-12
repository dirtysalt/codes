#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        class Result:
            def __init__(self):
                self.op = None
                self.data: Result = None
                self.sz = 1

            def operate(self, op):
                r = Result()
                r.op = op
                r.data = self
                r.sz = self.sz * 2
                return r

            def find(self, k):
                if self.op is None:
                    assert k == 0, k
                    return 0

                sz = self.sz // 2
                c = self.data.find(k - sz if k >= sz else k)
                if self.op == 1 and k >= sz:
                    c = (c + 1) % 26
                return c

        r = Result()
        for op in operations:
            r = r.operate(op)
        ans = r.find(k - 1)
        return chr(ans + ord('a'))


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, [0, 0, 0], 'a'),
    (10, [0, 1, 0, 1], 'b'),
]

aatest_helper.run_test_cases(Solution().kthCharacter, cases)

if __name__ == '__main__':
    pass
