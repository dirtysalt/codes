#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import itertools
from typing import List

class Solution:
    def coopDevelop(self, skills: List[List[int]]) -> int:
        from collections import defaultdict
        for ss in skills:
            ss.sort()
        skills.sort(key=lambda x: len(x))
        index = defaultdict(set)

        MOD = 10 ** 9 + 7
        ans = 0
        for i in range(len(skills)):
            ss = tuple(skills[i])
            a = set()
            for l in range(1, len(ss) + 1):
                for t in itertools.combinations(ss, l):
                    a |= index[t]
            # print(a)
            ans += (i - len(a))
            index[ss].add(i)
        ans = ans % MOD
        return ans

true, false, null = True, False, None
cases = [
    ([[1, 2, 3], [3], [2, 4]], 2),
    ([[2], [3, 5, 7], [2, 3, 5, 6], [3, 4, 8], [2, 6], [3, 4, 8], [3]], 13)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().coopDevelop, cases)

if __name__ == '__main__':
    pass
