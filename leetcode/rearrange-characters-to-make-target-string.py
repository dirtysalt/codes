#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        def count(s):
            v = [0] * 26
            for c in s:
                x = ord(c) - ord('a')
                v[x] += 1
            return v

        A = count(s)
        B = count(target)

        ans = 10000
        for i in range(26):
            if B[i] == 0: continue
            x = A[i] // B[i]
            ans = min(ans, x)

        return ans


if __name__ == '__main__':
    pass
