#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def make_ft(s):
            ft = [0] * 26
            for c in s:
                ft[ord(c) - ord('a')] += 1
            return ft

        ft = make_ft(s1)
        ft2 = [0] * 26

        j = 0
        ans = False
        for i, c in enumerate(s2):
            x = ord(c) - ord('a')
            ft2[x] += 1

            if ft2[x] == ft[x]:
                if ft2 == ft:
                    ans = True
                    break

            while j <= i and ft2[x] > ft[x]:
                x2 = ord(s2[j]) - ord('a')
                ft2[x2] -= 1
                j += 1

        return ans
