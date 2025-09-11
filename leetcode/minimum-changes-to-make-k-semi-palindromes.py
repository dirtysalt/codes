#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        def fix_cost(i, j, d):
            sz = (j - i + 1)
            assert sz % d == 0
            c = 0
            for idx in range(d):
                ss = s[i + idx:j + 1:d]
                a, b = 0, len(ss) - 1
                while a < b:
                    if ss[a] != ss[b]:
                        c += 1
                    a += 1
                    b -= 1
            return c

        cost = {}
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                sz = j - i + 1
                res = sz
                for d in range(1, sz):
                    if sz % d == 0:
                        c = fix_cost(i, j, d)
                        res = min(res, c)
                cost[(i, j)] = res

        import functools
        @functools.cache
        def search(i, k):
            if i == len(s): return 0 if k == 0 else -1
            if k == 0: return -1
            ans = len(s)
            for j in range(i + 1, len(s)):
                c = search(j + 1, k - 1)
                if c == -1: continue
                ans = min(ans, c + cost[(i, j)])
            return ans

        return search(0, k)


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(s="abcac", k=2, res=1),
    aatest_helper.OrderedDict(s="abcdef", k=2, res=2),
    aatest_helper.OrderedDict(s="aabbaa", k=3, res=0),
    aatest_helper.OrderedDict(s="aaaaacabbb", k=1, res=3),
    ("rkyidomzyud", 3, 4),
]

aatest_helper.run_test_cases(Solution().minimumChanges, cases)

if __name__ == '__main__':
    pass
