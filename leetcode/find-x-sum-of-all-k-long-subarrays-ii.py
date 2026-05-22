#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findXSum(self, nums: List[int], K: int, X: int) -> List[int]:
        from collections import Counter
        from sortedcontainers import SortedList

        cnt = Counter(nums[:K])
        sl = SortedList()

        for k, v in cnt.items():
            sl.add((v, k))

        index = len(sl) - 1
        acc = 0
        for _ in range(X):
            if index < 0: break
            v = sl[index]
            index -= 1
            acc += v[0] * v[1]

        def update(k, v0, v1):
            nonlocal acc
            # remove v0, k pair
            if v0 > 0:
                index = sl.index((v0, k))
                if index >= len(sl) - X:
                    acc -= v0 * k
                    fill = len(sl) - X - 1
                    if fill >= 0:
                        t = sl[fill]
                        acc += t[0] * t[1]
                sl.remove((v0, k))

            # insert v1, k pair
            index = sl.bisect((v1, k))
            if index >= len(sl) - X + 1:
                acc += v1 * k
                expire = len(sl) - X
                if expire >= 0:
                    t = sl[expire]
                    acc -= t[0] * t[1]
            sl.add((v1, k))

        ans = [acc]
        for i in range(K, len(nums)):
            v = cnt[nums[i]]
            cnt[nums[i]] += 1
            update(nums[i], v, v + 1)
            v = cnt[nums[i - K]]
            cnt[nums[i - K]] -= 1
            update(nums[i - K], v, v - 1)
            ans.append(acc)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2, res=[6, 10, 12]),
    aatest_helper.OrderedDict(nums=[3, 8, 7, 8, 7, 5], k=2, x=2, res=[11, 15, 15, 15, 12]),
]

aatest_helper.run_test_cases(Solution().findXSum, cases)

if __name__ == '__main__':
    pass
