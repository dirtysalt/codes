#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        dedup = set()
        index = []
        for i, x in enumerate(elements):
            if x in dedup: continue
            index.append(i)
            dedup.add(x)

        n = len(groups)
        from collections import defaultdict
        value2ps = defaultdict(list)
        for i, x in enumerate(groups):
            value2ps[x].append(i)
        ans = [-1] * n

        M = max(groups)
        for i in index:
            x = elements[i]
            for j in range(1, M // x + 1):
                value = x * j
                if value in value2ps:
                    ps = value2ps[value]
                    del value2ps[value]
                    for p in ps:
                        ans[p] = i
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([8, 4, 3, 2, 4], [4, 2], [0, 0, -1, 1, 0]),
    ([2, 3, 5, 7], [5, 3, 3], [-1, 1, 0, -1]),
    ([10, 21, 30, 41], [2, 1], [0, 1, 0, 1]),
]

aatest_helper.run_test_cases(Solution().assignElements, cases)

if __name__ == '__main__':
    pass
