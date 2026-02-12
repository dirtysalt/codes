#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)

        keys = list(cnt.keys())
        keys.sort(reverse=True)
        depth = {}
        for x in keys:
            if x == 1:
                c = cnt[x]
                if c % 2 == 0:
                    c -= 1
                depth[x] = c
                continue

            if cnt[x] == 1:
                depth[x] = 1
                continue

            assert (cnt[x] >= 2)
            y = x * x
            if cnt[y] == 0:
                depth[x] = 1
            elif cnt[y] == 1:
                depth[x] = 3
            else:
                depth[x] = 2 + depth[y]

        ans = max(depth.values())
        return ans


if __name__ == '__main__':
    pass
