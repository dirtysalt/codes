#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for op in operations:
            if op[1] == '+':
                ans += 1
            else:
                ans -= 1
        return ans


if __name__ == '__main__':
    pass
