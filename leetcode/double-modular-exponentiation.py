#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:

        def pow(a, b, m):
            ans = 1
            while b:
                if b & 0x1:
                    ans = (ans * a) % m
                b >>= 1
                a = (a * a) % m
            return ans

        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            x = pow(a, b, 10)
            y = pow(x, c, m)
            if y == target:
                ans.append(i)
        return ans


if __name__ == '__main__':
    pass
