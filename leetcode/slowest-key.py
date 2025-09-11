#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        p = 0
        n = len(keysPressed)
        times = [0] * 26
        for i in range(n):
            t = releaseTimes[i] - p
            p = releaseTimes[i]
            c = ord(keysPressed[i]) - ord('a')
            times[c] = max(times[c], t)

        maxv = max(times)
        ans = 0
        for i in range(26):
            if times[i] == maxv:
                ans = i
        return chr(ans + ord('a'))
