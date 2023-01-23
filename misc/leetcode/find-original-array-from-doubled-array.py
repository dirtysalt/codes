#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        from collections import Counter
        used = Counter(changed)
        ans = []
        changed.sort()
        for x in changed:
            if used[x] == 0: continue
            used[x] -= 1
            x2 = x * 2
            if used[x2]:
                used[x2] -= 1
                ans.append(x)
            else:
                return []
        ans.sort()
        return ans


true, false, null = True, False, None
cases = [
    ([1, 3, 4, 2, 6, 8], [1, 3, 4]),
    ([0, 0], [0]),
    ([0], []),
    ([2, 1], [1]),
    ([2, 1, 2, 4, 2, 4], [1, 2, 2]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findOriginalArray, cases)

if __name__ == '__main__':
    pass
