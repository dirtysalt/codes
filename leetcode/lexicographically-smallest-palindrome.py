#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        i, j = 0, n - 1
        ans = [''] * n
        while i <= j:
            c = min(s[i], s[j])
            ans[i] = ans[j] = c
            i += 1
            j -= 1
        return ''.join(ans)


if __name__ == '__main__':
    pass
