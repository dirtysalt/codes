#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        def check(p):
            p2 = p
            for i in range(n - 1):
                p2 = p2 ^ derived[i]
            return p2 ^ p == derived[-1]

        return check(0) or check(1)


if __name__ == '__main__':
    pass
