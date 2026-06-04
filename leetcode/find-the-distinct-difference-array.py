#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        from collections import Counter
        a, b = Counter(), Counter(nums)
        ans = []
        for x in nums:
            a[x] += 1
            b[x] -= 1
            if b[x] == 0:
                del b[x]
            ans.append(len(a) - len(b))
        return ans


if __name__ == '__main__':
    pass
