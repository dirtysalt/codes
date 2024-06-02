#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def clearStars(self, s: str) -> str:
        from sortedcontainers import SortedList
        pos = [SortedList() for _ in range(27)]

        def tox(c):
            if c == '*': return 26
            return ord(c) - ord('a')

        for i, c in enumerate(s):
            pos[tox(c)].add(i)

        mask = set()
        for p in pos[26]:
            mask.add(p)
            for j in range(26):
                sl = pos[j]
                idx = sl.bisect_left(p)
                if idx == 0: continue
                rem = sl[idx - 1]
                sl.remove(rem)
                mask.add(rem)
                break

        ans = ''.join([c for (p, c) in enumerate(s) if p not in mask])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("aaba*", "aab"),
    ("abc", "abc"),
    ("aab*", "ab"),
]

aatest_helper.run_test_cases(Solution().clearStars, cases)

if __name__ == '__main__':
    pass
