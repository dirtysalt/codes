#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getSmallestString(self, s: str) -> str:
        ans = s
        ss = list(s)
        for i in range(1, len(s)):
            j = i - 1
            if ord(ss[i]) % 2 == ord(ss[j]) % 2:
                ss[i], ss[j] = ss[j], ss[i]
                ans = min(ans, ''.join(ss))
                ss[i], ss[j] = ss[j], ss[i]
        return ans


if __name__ == '__main__':
    pass
