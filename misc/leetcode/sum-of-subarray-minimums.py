#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = []
        n = len(arr)

        ans = 0
        for i in range(n):
            s = i
            while st and arr[i] < st[-1][0]:
                value, start, index = st.pop()
                ans += value * (index - start + 1) * (i - index)
                s = start
            st.append((arr[i], s, i))

        while st:
            value, start, index = st.pop()
            ans += value * (index - start + 1) * (n - index)

        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans


true, false, null = True, False, None
cases = [
    ([3, 1, 2, 4], 17),
    ([11, 81, 94, 43, 3], 444),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sumSubarrayMins, cases)

if __name__ == '__main__':
    pass
