#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos = []
        for i in range(len(nums)):
            if nums[i] == x:
                pos.append(i)

        ans = []
        for q in queries:
            p = pos[q - 1] if (q - 1) < len(pos) else -1
            ans.append(p)
        return ans


if __name__ == '__main__':
    pass
