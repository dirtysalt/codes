#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        cnt = Counter()
        for x in nums:
            cnt[x] += 1

        ans = []
        while cnt:
            ans.append([])
            d = ans[-1]
            for k in cnt.keys():
                d.append(k)
                cnt[k] -= 1

            for k in d:
                if cnt[k] == 0:
                    del cnt[k]
        return ans


if __name__ == '__main__':
    pass
