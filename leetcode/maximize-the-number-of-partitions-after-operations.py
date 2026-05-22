#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        ss = [ord(x) - ord('a') for x in s]

        @functools.cache
        def dfs(i, mask, changed):
            if i == len(ss): return 1

            def test(c):
                mask2 = mask | (1 << c)
                changed2 = changed | (c != ss[i])
                if mask2.bit_count() > k:
                    r = dfs(i + 1, (1 << c), changed2) + 1
                else:
                    r = dfs(i + 1, mask2, changed2)
                return r

            ans = 0
            if changed:
                ans = test(ss[i])
            else:
                for c in range(26):
                    r = test(c)
                    ans = max(ans, r)
            return ans

        ans = dfs(0, 0, False)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("accca", 2, 3),
    ("aabaab", 3, 1),
    ("xxyz", 1, 4),
]

aatest_helper.run_test_cases(Solution().maxPartitionsAfterOperations, cases)

if __name__ == '__main__':
    pass
