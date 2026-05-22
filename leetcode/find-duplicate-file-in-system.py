#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dup = defaultdict(list)

        for p in paths:
            ps = p.split()
            d = ps[0]
            for p2 in ps[1:]:
                f, c = p2.split('(')
                c = c[:-1]
                f = d + '/' + f
                dup[c].append(f)

        ans = []
        print(dup)
        for c, fs in dup.items():
            if len(fs) > 1:
                ans.append(fs)
        ans.sort(key =lambda x: -len(x))
        return ans


cases = [
    (["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"], [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().findDuplicate, cases)

if __name__ == '__main__':
    pass
