#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0

        def work(buf):
            n = len(buf)
            dp = []
            for x in buf:
                s, e = 0, len(dp) - 1
                while s <= e:
                    m = (s + e) // 2
                    if dp[m] > x:
                        e = m - 1
                    else:
                        s = m + 1
                # put to s
                if s == len(dp):
                    dp.append(x)
                else:
                    dp[s] = min(dp[s], x)
            return len(buf) - len(dp)

        ans = 0
        for i in range(k):
            j = i
            buf = []
            while j < len(arr):
                buf.append(arr[j])
                j += k
            ans += work(buf)
        return ans


true, false, null = True, False, None
cases = [
    ([12, 6, 12, 6, 14, 2, 13, 17, 3, 8, 11, 7, 4, 11, 18, 8, 8, 3], 1, 12),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kIncreasing, cases)

if __name__ == '__main__':
    pass
