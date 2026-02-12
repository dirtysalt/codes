#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumOperations(self, num: str) -> int:
        def search(a, b):
            i = len(num) - 1
            res = 0
            while i >= 0 and num[i] != a:
                res += 1
                i -= 1
            if i < 0: return -1
            i -= 1
            while i >= 0 and num[i] != b:
                res += 1
                i -= 1
            if i < 0: return -1
            return res

        num = '00' + num
        ans = len(num)
        for s in ('00', '25', '50', '75'):
            c = search(s[1], s[0])
            if c != -1:
                ans = min(ans, c)
        return ans


if __name__ == '__main__':
    pass
