#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        clips.insert(0, [0, 0])

        n = len(clips)
        inf = (1 << 30)
        dp = [0] * n
        ans = inf
        for i in range(1, n):
            (x, y) = clips[i]
            res = inf
            for j in range(i):
                if x <= clips[j][1]:
                    res = min(res, dp[j] + 1)
            dp[i] = res
            if y >= T:
                ans = min(ans, res)
        if ans == inf:
            ans = -1
        return ans
