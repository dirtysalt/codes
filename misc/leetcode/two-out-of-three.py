#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        cnt = [0] * 101

        for x in set(nums1):
            cnt[x] += 1
        for x in set(nums2):
            cnt[x] += 1
        for x in set(nums3):
            cnt[x] += 1

        ans = []

        for x in range(len(cnt)):
            if cnt[x] >= 2:
                ans.append(x)

        return ans


if __name__ == '__main__':
    pass
