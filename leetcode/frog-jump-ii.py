#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:

        n = len(stones)

        def test(k):
            mask = [0] * n

            # forward passing
            i = 0
            while i != n - 1:
                j = i + 1
                while j < n and (stones[j] - stones[i]) <= k:
                    j += 1
                j -= 1
                if j == i: return False
                mask[j] = 1
                i = j

            # backward passing
            assert i == (n - 1)
            while i != 0:
                j = i - 1
                while j >= 0 and mask[j] == 1: j -= 1
                assert mask[j] == 0
                if stones[i] - stones[j] > k: return False
                i = j

            return True

        s, e = 1, stones[-1]
        while s <= e:
            m = (s + e) // 2
            if test(m):
                e = m - 1
            else:
                s = m + 1
        return s


true, false, null = True, False, None
cases = [
    ([0, 2, 5, 6, 7], 5),
    ([0, 3, 9], 9),
    ([0, 3], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxJump, cases)

if __name__ == '__main__':
    pass
