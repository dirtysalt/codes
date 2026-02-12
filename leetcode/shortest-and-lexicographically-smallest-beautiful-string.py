#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = None
        n = len(s)
        for sz in range(1, n + 1):
            for i in range(n - sz + 1):
                c = 0
                for x in s[i:i + sz]:
                    if x == '1':
                        c += 1
                if c == k:
                    if ans is None:
                        ans = s[i:i + sz]
                    else:
                        ans = min(ans, s[i:i + sz])
            if ans: return ans
        return ""


if __name__ == '__main__':
    pass
