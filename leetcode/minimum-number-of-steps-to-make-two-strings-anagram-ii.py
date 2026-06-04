#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def dist(ss):
            cnt = [0] * 26
            for x in ss:
                c = ord(x) - ord('a')
                cnt[c] += 1
            return cnt

        a = dist(s)
        b = dist(t)
        ans = 0
        for i in range(26):
            ans += abs(a[i] - b[i])
        return ans

if __name__ == '__main__':
    pass
