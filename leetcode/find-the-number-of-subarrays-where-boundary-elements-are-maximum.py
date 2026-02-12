#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        ans = len(nums)
        st = []
        from collections import Counter
        cnt = Counter()

        for x in nums:
            while st and st[-1] < x:
                cnt[st[-1]] -= 1
                st.pop()
            ans += cnt[x]
            cnt[x] += 1
            st.append(x)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 4, 3, 3, 2], 6),
    ([3, 3, 3], 6),
    ([1], 1),
]

aatest_helper.run_test_cases(Solution().numberOfSubarrays, cases)

if __name__ == '__main__':
    pass
