#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:

        def next_one(nums):
            pos = [-1] * 10
            for i in reversed(range(len(nums))):
                x = nums[i]
                pos[x] = i
                swap = -1
                for y in range(x + 1, 10):
                    if pos[y] != -1:
                        swap = pos[y]
                        break

                if swap != -1:
                    nums[i], nums[swap] = nums[swap], nums[i]
                    # FIXME: optimization?
                    nums[i+1:] = sorted(nums[i+1:])
                    break

        ## FIXME:
        nums = [int(x) for x in num]
        old = nums.copy()

        for i in range(k):
            next_one(nums)


        ans = 0
        for i in range(len(old)):
            if old[i] == nums[0]:
                nums = nums[1:]
                continue

            swap = 0
            for j in range(1, len(nums)):
                if nums[j] == old[i]:
                    swap = j
                    break

            ans += swap
            nums = nums[:swap] + nums[swap+1:]
        return ans



cases = [
    ("5489355142", 4, 2),
    ("11112", 4, 4),
    ("00123", 1, 1),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().getMinSwaps, cases)


if __name__ == '__main__':
    pass
