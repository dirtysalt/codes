#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import Counter
from typing import List


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        child = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            child[p].append(i)

        cnt = Counter([0])

        def search(root, now):
            ans = 0
            for c in child[root]:
                bit = (1 << (ord(s[c]) - ord('a')))
                x = now ^ bit
                ans += cnt[x]
                for i in range(26):
                    ans += cnt[x ^ (1 << i)]
                cnt[x] += 1
                ans += search(c, x)
            return ans

        ans = search(0, 0)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([-1, 0, 0, 1, 1, 2], "acaabc", 8),
    ([-1, 0, 0, 0, 0], "aaaaa", 10),
    ([-1, 5, 0, 5, 5, 2], "xsbcqq", 7),
    ([-1, 0, 0, 0, 1, 3, 7, 2], "pxxgtgpp", 18),
]

cases += aatest_helper.read_cases_from_file('tmp.in', 3)
aatest_helper.PROFILE = false
aatest_helper.run_test_cases(Solution().countPalindromePaths, cases)

if __name__ == '__main__':
    pass
