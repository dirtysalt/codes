#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        from collections import Counter
        cnt = Counter()
        ways = set()
        K = len(nums)

        arr = []
        for w, xs in enumerate(nums):
            arr.extend([(x, w) for x in xs])
        arr.sort()

        min_dist = 1 << 30
        ans = None
        j = 0
        for i, (x, w) in enumerate(arr):
            cnt[w] += 1
            if cnt[w] == 1:
                ways.add(w)

            if len(ways) == K:
                while j <= i and len(ways) == K:
                    xx, ww = arr[j]
                    cnt[ww] -= 1
                    if cnt[ww] == 0:
                        ways.remove(ww)
                    j += 1

                begin = arr[j - 1][0]
                end = arr[i][0]
                if (end - begin) < min_dist:
                    min_dist = (end - begin)
                    ans = [begin, end]

        return ans


import aatest_helper

cases = [
    ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24]),
]
aatest_helper.run_test_cases(Solution().smallestRange, cases)
