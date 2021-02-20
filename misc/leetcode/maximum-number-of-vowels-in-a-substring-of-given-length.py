#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isOK(c):
            return c in 'aeiou'

        cnt = 0
        for i in range(k):
            if isOK(s[i]):
                cnt += 1
        ans = cnt

        for i in range(k, len(s)):
            if isOK(s[i - k]):
                cnt -= 1
            if isOK(s[i]):
                cnt += 1
            ans = max(ans, cnt)
        return ans
