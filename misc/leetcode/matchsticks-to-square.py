#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if n < 4 or s % 4 != 0:
            return False

        avg = s // 2
        nums.sort()

        def ok(ss, s):
            # print(ss)
            n = len(ss)

            for st in range(1, 1 << n - 1):
                t = 0
                for j in range(n):
                    if (st >> j) & 0x1:
                        t += ss[j]
                if t == (s - t):
                    return True

            return False

        def search(k, l, r, sl, sr):
            if k == n:
                return sl == sr and ok(l, sl) and ok(r, sr)

            x = nums[k]
            if sl != avg and (sl + x) > avg: return False
            if sl != avg and (sr + x) > avg: return False

            l.append(x)
            if search(k + 1, l, r, sl + x, sr):
                return True
            l.pop()

            r.append(x)
            if search(k + 1, l, r, sl, sr + x):
                return True
            r.pop()

            return False

        ans = search(0, [], [], 0, 0)
        return ans


cases = [
    ([1, 1, 2, 2, 2], True),
    ([5, 5, 5, 5, 16, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4], True),
    ([2, 2, 2, 2, 2, 2], True),
    (
        [6961655, 6721573, 5852338, 4455955, 7980746, 4533546, 1148969, 101844, 9721301, 4048728, 4397033, 2520627,
         2522511,
         6094454, 1023140], False),
    ([1569462, 2402351, 9513693, 2220521, 7730020, 7930469, 1040519, 5767807, 876240, 350944, 4674663, 4809943, 8379742,
      3517287, 8034755], False),
    ([6035753, 3826635, 922363, 6104805, 1189018, 6365253, 364948, 2725801, 5577769, 7857734, 2860709, 9554210, 4883540,
      8712121, 3545089], False)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().makesquare, cases)
