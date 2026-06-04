#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import defaultdict
        C = defaultdict(list)
        j = 0
        for i in range(len(s)):
            if s[i] != s[j]:
                sz = i - j
                C[s[j]].append(sz)
                j = i
        sz = len(s) - j
        C[s[j]].append(sz)

        def compute(sizes):
            ans = -1
            sizes.sort(reverse=True)
            if len(sizes) >= 1:
                if sizes[0] >= 3:
                    ans = max(ans, sizes[0] - 2)
            if len(sizes) >= 2:
                if sizes[0] >= 2:
                    ans = max(ans, min(sizes[0] - 1, sizes[1]))
            if len(sizes) >= 3:
                ans = max(ans, min(sizes[0], sizes[1], sizes[2]))
            # print(sizes, ans)
            return ans

        ans = -1
        for c, sizes in C.items():
            r = compute(sizes)
            ans = max(ans, r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("aaaa", 2),
    ("abcdef", -1),
    ("abcaba", 1),
    ("fafff", 1),
]

aatest_helper.run_test_cases(Solution().maximumLength, cases)

if __name__ == '__main__':
    pass
