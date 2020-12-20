#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        nums = nums[::-1]

        n = len(nums)
        most_idx = n - 1
        swap = None
        for i in reversed(range(n - 1)):
            if nums[i] > nums[most_idx]:
                most_idx = i
            elif nums[i] < nums[most_idx]:
                swap = i, most_idx

        if swap:
            x, y = swap
            nums[x], nums[y] = nums[y], nums[x]

        print(nums)
        ans = 0
        for i in range(len(nums)):
            ans = ans * 10 + nums[i]
        return ans
