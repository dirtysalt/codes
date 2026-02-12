#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        dp = [0] * (len(word1) + 1)
        for i in reversed(range(len(word1))):
            sz = dp[i + 1]
            if sz < len(word2) and word1[i] == word2[len(word2) - 1 - sz]:
                dp[i] = sz + 1
            else:
                dp[i] = sz
        # print(dp)

        i, j = 0, 0
        pos = []
        k = 1
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                pos.append(i)
                j += 1
            elif k > 0:
                # word1[i] fixed to match word2[j]:
                # and word1[i+1] can cover word2[j+1]
                if dp[i + 1] >= len(word2) - 1 - j:
                    k -= 1
                    pos.append(i)
                    j += 1
            i += 1
        if j != len(word2):
            pos.clear()
        return pos


true, false, null = True, False, None
import aatest_helper

cases = [
    ("ciaigggwhhefeeg", "ggihh", [4, 5, 6, 8, 9]),
    ("ggwhh", "ggihh", [0, 1, 2, 3, 4]),
    ("ccbccccbcc", "b", [0]),
]

aatest_helper.run_test_cases(Solution().validSequence, cases)

if __name__ == '__main__':
    pass
