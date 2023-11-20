#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        black = 0
        ans = 0
        for i in reversed(range(n)):
            if s[i] == '1':
                # move i to (n-black-1)
                step = n - black - 1 - i
                black += 1
                ans += step
            else:
                pass
        return ans


if __name__ == '__main__':
    pass
