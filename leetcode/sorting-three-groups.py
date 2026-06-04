#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        import functools
        @functools.cache
        def search(i, last):
            if i == len(nums): return 0

            ans = 10000
            if nums[i] < last:
                # change to last?
                c = 1 + search(i + 1, last)
                ans = min(ans, c)
            else:
                for x in range(last, nums[i] + 1):
                    c = search(i + 1, x)
                    if x != nums[i]:
                        c += 1
                    ans = min(ans, c)
            return ans

        ans = search(0, 1)
        return ans


if __name__ == '__main__':
    pass
