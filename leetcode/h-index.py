#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# note(yan): 这个逻辑稍微有点绕。二分搜索最好还是自己手写!
class Solution:
    def hIndex(self, citations):
        citations.sort()
        if not citations or citations[-1] == 0:
            return 0

        n = len(citations)

        # try m as h-index
        s, e = 1, n
        ans = 0
        while s <= e:
            m = (s + e) // 2
            if citations[n - m] >= m:
                ans = max(ans, m)
                s = m + 1
            else:
                e = m - 1
        return ans


cases = [
    ([3, 0, 6, 1, 5], 3)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().hIndex, cases)
