#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        from collections import Counter
        cnt = Counter()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                cnt[nums[i + 1]] += 1
        return cnt.most_common(1)[0][0]



if __name__ == '__main__':
    pass
