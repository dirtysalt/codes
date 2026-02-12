#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        def fix(x, y):
            t = x // y
            while True:
                z = x // t
                rem = x % t
                z2 = z
                if rem:
                    z2 += 1
                if z2 <= y:
                    return z, t - 1
                t += 1

        t = nums[-1]
        ans = 0
        for x in reversed(nums):
            if x > t:
                t, c = fix(x, t)
                ans += c
            else:
                t = x
        return ans


true, false, null = True, False, None
cases = [
    ([3, 9, 3], 2),
    ([1, 2, 3, 4, 5], 0),
    ([368, 112, 2, 282, 349, 127, 36, 98, 371, 79, 309, 221, 175, 262, 224, 215, 230, 250, 84, 269, 384, 328, 118, 97,
      17, 105, 342, 344, 242, 160, 394, 17, 120, 335, 76, 101, 260, 244, 378, 375, 164, 190, 320, 376, 197, 398, 353,
      138, 362, 38, 54, 172, 3, 300, 264, 165, 251, 24, 312, 355, 237, 314, 397, 101, 117, 268, 36, 165, 373, 269, 351,
      67, 263, 332, 296, 13, 118, 294, 159, 137, 82, 288, 250, 131, 354, 261, 192, 111, 16, 139, 261, 295, 112, 121,
      234, 335, 256, 303, 328, 242, 260, 346, 22, 277, 179, 223], 17748),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumReplacement, cases)

if __name__ == '__main__':
    pass
