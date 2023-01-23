#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        j = 0
        ans = 0
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                pass
            else:
                ans = max(ans, i - j)
                j = i
        ans = max(ans, len(s) - j)
        return ans


if __name__ == '__main__':
    pass
