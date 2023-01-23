#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        def work(startIndex):
            ans = 0;
            r, c = startPos
            for x in s[startIndex:]:
                if x == 'R':
                    c += 1
                elif x == 'L':
                    c -= 1
                elif x == 'U':
                    r -= 1
                else:
                    r += 1
                if 0 <= r < n and 0 <= c < n:
                    ans += 1
                else:
                    break
            return ans

        ans = [0] * len(s)
        for i in range(len(s)):
            res = work(i)
            ans[i] = res

        return ans


if __name__ == '__main__':
    pass
