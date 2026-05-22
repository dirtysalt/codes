#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        from collections import defaultdict
        back = defaultdict(set)

        for x in nums:
            back[x].add(x)

        for f, t in zip(moveFrom, moveTo):
            if f == t: continue
            old = back[f]
            back[t].update(old)
            back[f].clear()

        map = {}
        for t, old in back.items():
            for f in old:
                map[f] = t

        ans = set()
        for x in nums:
            ans.add(map[x])
        ans = list(ans)
        ans.sort()
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 6, 7, 8], [1, 7, 2], [2, 9, 5], [5, 6, 8, 9]),
    ([1, 1, 3, 3], [1, 3], [2, 2], [2]),
    ([3, 4],
     [4, 3, 1, 2, 2, 3, 2, 4, 1],
     [3, 1, 2, 2, 3, 2, 4, 1, 1],
     [1])
]

aatest_helper.run_test_cases(Solution().relocateMarbles, cases)

if __name__ == '__main__':
    pass
