#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = arr.copy()
        n = len(arr)
        ans[-1] = -1
        for i in reversed(range(n-1)):
            ans[i] = max(ans[i+1], arr[i+1])
        return ans


cases = [
    ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1])
]

import aatest_helper
aatest_helper.run_test_cases(Solution().replaceElements, cases)
