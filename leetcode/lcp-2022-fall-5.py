#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def unSuitability(self, operate: List[int]) -> int:
        inf = 1 << 30
        mx = max(operate) * 2
        pre = [inf] * (mx + 1)
        pre[0] = 0

        for x in operate:
            dp = [inf] * (mx + 1)
            for off, value in enumerate(pre):
                if value == inf: continue
                if (off + x) <= mx:
                    dp[off + x] = min(dp[off + x], max(value, off + x))
                if off >= x:
                    dp[off - x] = min(dp[off - x], value)
                else:
                    dp[0] = min(dp[0], value + x - off)
            pre = dp

        return min(pre)


class Solution:
    def unSuitability(self, operate: List[int]) -> int:
        low = 1
        high = max(operate) * 2

        def check(mid):
            mask = 2 ** (mid + 1) - 1
            t = mask
            for x in operate:
                t = ((t << x) | (t >> x)) & mask
            return t != 0

        while low <= high:
            mid = (high + low) // 2
            ok = check(mid)
            if not ok:
                low = mid + 1
            else:
                high = mid - 1

        return low


true, false, null = True, False, None
cases = [
    ([5, 3, 7], 8),
    ([20, 10], 20),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().unSuitability, cases)

if __name__ == '__main__':
    pass
