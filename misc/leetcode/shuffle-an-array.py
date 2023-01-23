#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.fac = [1]
        for i in range(2, len(nums) + 1):
            self.fac.append(i * self.fac[-1])

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        if not self.nums:
            return []

        arr = self.nums[:]
        res = []
        n = random.randint(0, self.fac[-1] - 1)
        for i in reversed(range(len(self.fac) - 1)):
            idx = n // self.fac[i]
            n %= self.fac[i]
            res.append(arr[idx])
            arr.pop(idx)
        res.append(arr.pop())
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

sol = Solution([1, 2, 3, 4, 5])
print(sol.shuffle())
