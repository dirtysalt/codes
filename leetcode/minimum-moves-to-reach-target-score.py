#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        dd = 0
        while target != 1 and dd < maxDoubles:
            if target % 2 == 0:
                dd += 1
                target //= 2
            else:
                target -= 1
            ans += 1

        ans += (target - 1)
        return ans


if __name__ == '__main__':
    pass
