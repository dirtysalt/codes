#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestNumber(self, num: int) -> int:
        flip = False
        if num < 0:
            flip = True
            num = -num
        ds = []
        while num:
            x = num % 10
            ds.append(x)
            num //= 10

        ds.sort(reverse=flip)
        if not flip and ds and ds[0] == 0:
            for i in range(len(ds)):
                if ds[i] != 0:
                    ds[i], ds[0] = ds[0], ds[i]
                    break

        ans = 0
        for d in ds:
            ans = ans * 10 + d
        if flip:
            ans = -ans
        return ans


true, false, null = True, False, None
cases = [
    (310, 103),
    (-7605, -7650),
    (0, 0),
    (-0, 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallestNumber, cases)

if __name__ == '__main__':
    pass
