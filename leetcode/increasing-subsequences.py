#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def dfs(i, tmp):
            if i == len(nums):
                return

            if not tmp or nums[i] >= tmp[-1]:
                tmp.append(nums[i])
                if len(tmp) >= 2:
                    t = tuple(tmp)
                    ans.add(t)
                dfs(i + 1, tmp)
                tmp.pop()

            dfs(i + 1, tmp)

        dfs(0, [])
        ans = [list(x) for x in ans]
        # print(ans)
        return ans


class Solution2:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        def dfs(i, tmp):
            if i == len(nums):
                return

            x = nums[i]
            j = i
            while j < len(nums) and nums[j] == x:
                j += 1
            sz = (j - i)

            if not tmp or x >= tmp[-1]:
                for _ in range(sz):
                    tmp.append(x)
                    if len(tmp) >= 2:
                        ans.append(tmp.copy())
                    dfs(j, tmp)
                for _ in range(sz):
                    tmp.pop()
            dfs(j, tmp)

        dfs(0, [])
        # print(ans)
        return ans


import aatest_helper

cases = [
    ([4, 6, 7, 7], aatest_helper.ANYTHING)
]

aatest_helper.run_test_cases(Solution().findSubsequences, cases)
