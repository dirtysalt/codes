#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import Counter
        cnt = Counter()
        for xs in wall:
            acc = 0
            for x in xs:
                acc += x
                cnt[acc] += 1
            # 结尾的edge需要切掉
            cnt[acc] -= 1

        n = len(wall)
        ans = n
        if cnt:
            t, c = cnt.most_common(1)[0]
            ans = n - c
        return ans
