#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        pos = [[] for _ in range(26)]
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            pos[c].append(i)

        # print(pos)
        ans = 0
        req = [k - 1] * 26
        for i in range(len(s)):
            p = len(s)
            for j in range(26):
                if req[j] < len(pos[j]):
                    p = min(p, pos[j][req[j]])
            ans += (len(s) - p)
            req[ord(s[i]) - ord('a')] += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("abacb", 2, 4),
    ("abcde", 1, 15),
]

aatest_helper.run_test_cases(Solution().numberOfSubstrings, cases)

if __name__ == '__main__':
    pass
