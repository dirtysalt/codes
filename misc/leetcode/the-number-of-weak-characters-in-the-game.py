#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        if not properties: return 0
        props = [tuple(x) for x in properties]
        props.sort()

        import sortedcontainers
        sl = sortedcontainers.SortedList()
        for x, y in props:
            sl.add(y)

        j = 0
        n = len(props)
        ans = 0

        for x, y in props:
            while j < n and props[j][0] == x:
                sl.remove(props[j][1])
                j += 1

            if j == n:
                continue

            if sl[-1] > y:
                ans += 1

        return ans


true, false, null = True, False, None
cases = [
    ([[5, 5], [6, 3], [3, 6]], 0),
    ([[2, 2], [3, 3]], 1),
    ([[1, 5], [10, 4], [4, 3]], 1),
    ([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfWeakCharacters, cases)

if __name__ == '__main__':
    pass
