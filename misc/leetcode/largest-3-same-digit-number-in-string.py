#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def largestGoodInteger(self, num: str) -> str:

        ans = ""
        for i in range(0, len(num) - 2):
            s = num[i:i + 3]
            if s[0] == s[1] == s[2]:
                ans = max(ans, s)
        return ans


if __name__ == '__main__':
    pass
