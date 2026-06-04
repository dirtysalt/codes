#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def compute(hs):
            values = [0] * len(hs)
            st = []
            for i in range(len(hs)):
                while st and hs[i] < hs[st[-1]]:
                    st.pop()
                if not st:
                    values[i] = hs[i] * (i + 1)
                else:
                    j = st[-1]
                    values[i] = values[j] + hs[i] * (i - j)
                st.append(i)
            return values

        left = compute(maxHeights)
        right = compute(maxHeights[::-1])
        right = right[::-1]
        ans = 0
        for i in range(len(maxHeights)):
            c = left[i] + right[i] - maxHeights[i]
            ans = max(ans, c)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([5, 3, 4, 1, 1], 13),
    ([6, 5, 3, 9, 2, 7], 22),
    ([3, 2, 5, 5, 2, 3], 18),
    ([1, 5, 2, 5, 6, 4, 6, 3, 4, 5], 33),
]

aatest_helper.run_test_cases(Solution().maximumSumOfHeights, cases)

if __name__ == '__main__':
    pass
