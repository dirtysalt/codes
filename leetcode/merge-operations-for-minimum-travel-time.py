#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        inf = (1 << 63) - 1
        time_prefix = [0] + time.copy()
        for i in range(1, len(time_prefix)):
            time_prefix[i] += time_prefix[i - 1]

        import functools
        @functools.cache
        def search(i, last_merge, k):
            if i == (n - 1):
                if k == 0: return 0
                return inf

            ans = inf
            # t = sum(time[last_merge:i + 1])
            t = time_prefix[i + 1] - time_prefix[last_merge]
            for j in range(i + 1, n):
                delta = (j - i - 1)
                cost = t * (position[j] - position[i])
                if cost >= ans: continue
                res = cost + search(j, i + 1, k - delta)
                ans = min(ans, res)

            return ans

        ans = search(0, 0, k)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(l=10, n=4, k=1, position=[0, 3, 8, 10], time=[5, 8, 3, 6], res=62),
    aatest_helper.OrderedDict(l=5, n=5, k=1, position=[0, 1, 2, 3, 5], time=[8, 3, 9, 3, 3], res=34),
]

aatest_helper.run_test_cases(Solution().minTravelTime, cases)

if __name__ == '__main__':
    pass
