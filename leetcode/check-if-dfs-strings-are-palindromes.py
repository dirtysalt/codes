#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        child = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p == -1: continue
            child[p].append(i)

        # BASE = 13131
        BASE = 10
        MOD = 151217133020331712151

        def pow(a, b):
            r = 1
            t = a
            while b:
                if b & 0x1:
                    r = (r * t) % MOD
                t = (t * t) % MOD
                b = b >> 1
            return r

        def dfs(x, digest):
            digest[x] = ord(s[x]) - ord('a')
            if not child[x]:
                return 1

            t = 0
            it = child[x]
            sz = 0
            for y in it:
                size = dfs(y, digest)
                # t * (BASE ** size)
                t = t * pow(BASE, size) + digest[y]
                sz += size
            t = t * BASE + digest[x]
            sz += 1
            digest[x] = t % MOD
            return sz

        def xdfs(x, digest):
            digest[x] = ord(s[x]) - ord('a')
            if not child[x]:
                return 1

            t = 0
            it = reversed(child[x])
            t = t * BASE + digest[x]
            sz = 1
            for y in it:
                size = xdfs(y, digest)
                # t * (BASE ** size)
                t = t * pow(BASE, size) + digest[y]
                sz += size
            digest[x] = t % MOD
            return sz

        d0 = [0] * n
        d1 = [0] * n
        dfs(0, d0)
        xdfs(0, d1)
        # print(d0, d1)
        ans = []
        for i in range(n):
            ans.append(d0[i] == d1[i])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([-1, 0, 0, 1, 1, 2], "aababa", [true, true, false, true, true, true]),
    ([-1, 0, 0, 0, 0], "aabcb", [true, true, true, true, true]),
]

aatest_helper.run_test_cases(Solution().findAnswer, cases)

if __name__ == '__main__':
    pass
