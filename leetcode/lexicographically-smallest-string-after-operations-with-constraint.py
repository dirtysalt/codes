#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def dist(a, b):
            a, b = ord(a) - ord('a'), ord(b) - ord('a')
            a, b = min(a, b), max(a, b)
            return min(b - a, a + 26 - b)

        ans = list(s)
        for i in range(len(ans)):
            if k == 0: break
            import string
            for c in string.ascii_lowercase:
                d = dist(c, ans[i])
                if k >= d:
                    ans[i] = c
                    k -= d
                    break

        return ''.join(ans)


true, false, null = True, False, None
import aatest_helper

cases = [
    ("zbbz", 3, "aaaz"),
    ("xaxcd", 4, "aawcd"),
    ("lol", 0, "lol")
]

aatest_helper.run_test_cases(Solution().getSmallestString, cases)

if __name__ == '__main__':
    pass
