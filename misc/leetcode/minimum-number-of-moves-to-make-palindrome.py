#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        ans = 0
        while s and len(s) != 1:
            I, J = 0, 0
            for j in reversed(range(len(s))):
                if s[j] == s[0]:
                    J = j
                    break
            for i in range(len(s)):
                if s[i] == s[-1]:
                    I = i
                    break

            if I < len(s) - 1 - J:
                ans += I
                s = s[:I] + s[I + 1:-1]

            else:
                ans += len(s) - 1 - J
                s = s[1:J] + s[J + 1:]

        return ans


true, false, null = True, False, None
cases = [
    ("aabb", 2),
    ("letelt", 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minMovesToMakePalindrome, cases)

if __name__ == '__main__':
    pass
