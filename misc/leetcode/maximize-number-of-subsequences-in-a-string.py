#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:

        def search(s):
            tail = 0
            for c in s:
                if c == pattern[1]:
                    tail += 1
            ans = 0
            for c in s:
                if c == pattern[1]:
                    tail -= 1
                if c == pattern[0]:
                    ans += tail
            return ans

        A = search(pattern[0] + text)
        B = search(text + pattern[1])
        ans = max(A, B)
        return ans


true, false, null = True, False, None
cases = [
    ("abdcdbc", "ac", 4),
    ("aabb", "ab", 6),
    ("aa", "aa", 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumSubsequenceCount, cases)

if __name__ == '__main__':
    pass
