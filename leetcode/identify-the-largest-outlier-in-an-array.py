#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import Counter
from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        total = sum(nums)
        ans = - (1 << 30)
        for x in nums:
            r = (total - x)
            cnt[x] -= 1
            if r % 2 == 0:
                r2 = r // 2
                if cnt[r2]:
                    ans = max(ans, x)
            cnt[x] += 1
        return ans


if __name__ == '__main__':
    pass
