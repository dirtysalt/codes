#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = (n + 1)
        for i in range(n):
            if words[i] == target:
                r0 = abs(i - startIndex)
                r1 = n - r0
                ans = min(ans, r0, r1)
        if ans == (n + 1):
            ans = -1
        return ans


if __name__ == '__main__':
    pass
