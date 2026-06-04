#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def values(x):
            res = []
            res.append(x)
            x = list(str(x))
            for i in range(len(x)):
                for j in range(i + 1, len(x)):
                    x[i], x[j] = x[j], x[i]
                    res.append(int(''.join(x)))
                    x[i], x[j] = x[j], x[i]
            return set(res)

        nums.sort(key=lambda x: len(str(x)))
        from collections import Counter
        cnt = Counter()

        ans = 0
        for x in nums:
            res = values(x)
            for r in res:
                ans += cnt[r]
            cnt[x] += 1
        return ans


if __name__ == '__main__':
    pass
