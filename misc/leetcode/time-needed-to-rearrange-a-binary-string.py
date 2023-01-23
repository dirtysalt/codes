#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        def op(s):
            n = len(s)
            res, i, swap = '', 0, 0
            while i < (n - 1):
                if s[i:i + 2] == '01':
                    res += '10'
                    i += 2
                    swap += 1
                else:
                    res += s[i]
                    i += 1
            if i == (n - 1):
                res += s[-1]
            return res, swap

        ans = 0
        while True:
            s2, swap = op(s)
            if swap == 0: break
            s = s2
            ans += 1
        return ans


if __name__ == '__main__':
    pass
