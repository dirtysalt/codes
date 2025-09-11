#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        st = []
        ans = 0
        for x in nums:
            now = 0
            while st and x >= st[-1][0]:
                p, c = st.pop()
                now = max(now, c)
            if st:
                st.append((x, now + 1))
                ans = max(ans, now + 1)
            else:
                st.append((x, 0))
            # print(st)
        return ans


true, false, null = True, False, None
cases = [
    ([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11], 3),
    ([4, 5, 7, 7, 13], 0),
    ([10, 1, 2, 3, 4, 5, 6, 1, 2, 3], 6),
    ([5, 11, 7, 8, 11], 2),
    ([10, 6, 5, 10, 15], 1),
    ([5, 3, 11], 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().totalSteps, cases)

if __name__ == '__main__':
    pass
