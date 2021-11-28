#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)

        ans.extend([-1] * k)
        acc = sum(nums[:2 * k])
        for i in range(k, n - k):
            acc += nums[i + k]
            avg = acc // (2 * k + 1)
            ans.append(avg)
            acc -= nums[i - k]

        ans.extend([-1] * k)
        ans = ans[:n]
        return ans


if __name__ == '__main__':
    pass
