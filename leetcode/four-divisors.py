#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        cnt = {}
        n = max(nums)

        for i in range(2, int(n ** 0.5) + 2):
            cnt[i * i] = 0

            for j in range(i + 1, n // i + 1):
                x = i * j
                if x not in cnt:
                    cnt[x] = i + j + x + 1
                else:
                    cnt[x] = 0

        # print(len([x for x in cnt if cnt[x]]))
        # print(cnt)
        ans = 0
        for x in nums:
            res = cnt.get(x, 0)
            ans += res

        return ans


cases = [
    ([21, 4, 7], 32),
    ([25, 4, 7], 0),
    ([35, ], 48),
    ([36, ], 0),
    ([100000, ], 0),
    ([1], 0),
    ([2], 0),
    ([3], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 45),
    ([389 ** 2, ], 0),
    ([16], 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sumFourDivisors, cases)
