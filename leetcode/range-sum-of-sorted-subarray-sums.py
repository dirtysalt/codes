#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        tmp = []
        for i in range(len(nums)):
            t = 0
            for j in range(i, len(nums)):
                t += nums[j]
                tmp.append(t)
        tmp.sort()
        # print(tmp)
        ans = sum(tmp[left - 1:right])
        MOD = 10 ** 9 + 7
        return ans % MOD


if __name__ == '__main__':
    pass
