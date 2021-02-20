#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# note(yan): 可以证明，序列S(支持全排列)和字符c，如果c和S中任意一个字符允许swap的话
# 那么S+c也可以组成全排列。也就是以为这swap位置是具有传递性的

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ps = list(range(len(s)))

        def findp(u):
            while ps[u] != u:
                u = ps[u]
            return u

        for u, v in pairs:
            up = findp(u)
            vp = findp(v)
            if up != vp:
                if up < vp:
                    ps[vp] = up
                else:
                    ps[up] = vp

        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(len(s)):
            p = findp(i)
            groups[p].append(i)

        ans = list(s)
        for ps in groups.values():
            if len(ps) == 1: continue
            tmp = [s[i] for i in ps]
            tmp.sort()
            for k in range(len(ps)):
                ans[ps[k]] = tmp[k]
        ans = ''.join(ans)
        return ans


cases = [
    ("dcab", [[0, 3], [1, 2], [0, 2]], 'abcd'),
    ("cba", [[0, 1], [1, 2]], 'abc')
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallestStringWithSwaps, cases)
