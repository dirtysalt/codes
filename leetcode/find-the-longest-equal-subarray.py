#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        def test(K):
            from collections import Counter
            cnt = Counter()
            step = min(K + k, len(nums))

            for i in range(step):
                x = nums[i]
                cnt[x] += 1
                if cnt[x] >= K: return True

            for i in range(step, len(nums)):
                cnt[nums[i]] += 1
                cnt[nums[i - step]] -= 1
                if cnt[nums[i]] >= K: return True
            return False

        s, e = 0, len(nums)
        while s <= e:
            K = (s + e) // 2
            if test(K):
                s = K + 1
            else:
                e = K - 1
        return e


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 3, 2, 3, 1, 3], 3, 3),
    ([1, 1, 2, 2, 1, 1], 2, 4),
    ([3, 2, 4, 2], 1, 2)
]

aatest_helper.run_test_cases(Solution().longestEqualSubarray, cases)

if __name__ == '__main__':
    pass
