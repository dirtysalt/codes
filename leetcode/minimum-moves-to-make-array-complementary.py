#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        from collections import Counter
        minx = []
        maxx = []
        cnt = Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            minx.append(min(a, b))
            maxx.append(max(a, b))
            cnt[a + b] += 1
        minx.sort()
        maxx.sort()

        ans = n
        for k, v in cnt.items():
            # if min_value -> limit, but limit + max_value < k
            # the change 2 items.
            # threshold = k - limit
            # max_value < k - limit

            c2 = 0
            threshold = k - limit
            s, e = 0, len(maxx) - 1
            while s <= e:
                m = (s + e) // 2
                if maxx[m] >= threshold:
                    e = m - 1
                else:
                    s = m + 1
            c2 += s

            # if max_value -> 1, but 1 + min_value > k
            # then change 2 items.
            # threshold = k - 1
            # min_value > k - 1
            threshold = k - 1
            s, e = 0, len(minx) - 1
            while s <= e:
                m = (s + e) // 2
                if minx[m] <= threshold:
                    s = m + 1
                else:
                    e = m - 1
            c2 += len(minx) - s

            c1 = (n // 2 - v - c2)
            cost = c1 * 1 + c2 * 2
            ans = min(ans, cost)
        return ans


cases = [
    ([1, 2, 4, 3], 4, 1),
    ([1, 2, 2, 1], 2, 2),
    ([1, 2, 1, 2], 2, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minMoves, cases)
