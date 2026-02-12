#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        from collections import Counter

        def position(guess):
            cnt = Counter()
            ans = 0
            j = 0
            for i in range(len(nums)):
                cnt[nums[i]] += 1
                while j <= i and len(cnt) > guess:
                    x = nums[j]
                    cnt[x] -= 1
                    if cnt[x] == 0:
                        del cnt[x]
                    j += 1
                ans += (i - j + 1)
            return ans

        s, e = 1, len(nums)
        total = (1 + len(nums)) * len(nums) // 2
        exp = (total + 1) // 2
        while s <= e:
            m = (s + e) // 2
            k = position(m)
            # print(s, e, m, k, exp)
            if k >= exp:
                e = m - 1
            else:
                s = m + 1
        return s


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3], 1),
    ([3, 4, 3, 4, 5], 2),
    ([4, 3, 5, 4], 2),
    ([91, 64, 76, 18, 61, 55, 46, 93, 65, 99], 4),
]

aatest_helper.run_test_cases(Solution().medianOfUniquenessArray, cases)

if __name__ == '__main__':
    pass
