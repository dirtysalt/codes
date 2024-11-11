#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        from collections import Counter
        cnt = Counter(nums)
        tmp = sorted(nums)
        cand = sorted(set([x - k for x in nums] + [x + k for x in nums] + nums))
        # print(cand)

        n = len(nums)
        i, j = 0, 0
        ans = 0
        for c in cand:
            while i < n and tmp[i] + k < c:
                i += 1
            while j < n and tmp[j] - k <= c:
                j += 1
            sz = min(numOperations, j - i - cnt[c]) + cnt[c]
            # print(c, sz)
            ans = max(ans, sz)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 4, 5], k=1, numOperations=2, res=2),
    aatest_helper.OrderedDict(nums=[5, 11, 20, 20], k=5, numOperations=1, res=2),
    ([88, 53], 27, 2, 2),
]

aatest_helper.run_test_cases(Solution().maxFrequency, cases)

if __name__ == '__main__':
    pass
