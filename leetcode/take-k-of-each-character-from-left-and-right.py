#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0

        ss = [ord(c) - ord('a') for c in s]
        n = len(ss)
        cnt = [0] * 3

        def ok():
            return cnt[0] >= k and cnt[1] >= k and cnt[2] >= k

        # 先从后面找到满足条件的j
        j = n - 1
        while j >= 0:
            cnt[ss[j]] += 1
            if ok(): break
            j -= 1
        if j == -1: return -1
        # 从后面找到的j的话，说明需要取(n-j)个
        ans = n - j

        # 然后从前开始逐个取，j开始后移，但是需要cnt[i] >= k.
        for i in range(n):
            cnt[ss[i]] += 1
            assert (ok())
            while j < n:
                cnt[ss[j]] -= 1
                if not ok():
                    cnt[ss[j]] += 1
                    break
                else:
                    j += 1
            r = (i + 1) + (n - j)
            ans = min(ans, r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("aabaaaacaabc", 2, 8),
    ("a", 1, -1),
    ("a", 0, 0),
    ("acbcc", 1, 3),
    ("aabaaaacaabc", 2, 8),
]

aatest_helper.run_test_cases(Solution().takeCharacters, cases)

if __name__ == '__main__':
    pass
