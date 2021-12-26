#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        from collections import defaultdict
        pos = defaultdict(list)
        for i in range(len(arr)):
            x = arr[i]
            pos[x].append(i)

        buf = {}
        for x in pos.keys():
            ps = pos[x]
            tt = sum(ps)
            right = len(ps)
            last = 0
            values = []
            for i in range(len(ps)):
                diff = ps[i] - last
                tt -= right * diff
                tt += (len(ps) - right) * diff
                values.append(tt)
                last = ps[i]
                right -= 1

            values = values[::-1]
            buf[x] = values

        ans = []
        for x in arr:
            ans.append(buf[x].pop())

        return ans


true, false, null = True, False, None
cases = [
    ([2, 1, 3, 1, 2, 3, 3], [4, 2, 7, 2, 4, 4, 5]),
    ([10, 5, 10, 10], [5, 0, 3, 4]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getDistances, cases)

if __name__ == '__main__':
    pass
