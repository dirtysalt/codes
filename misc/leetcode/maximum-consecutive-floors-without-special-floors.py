#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        ev = []
        ev.append((bottom, 0))
        ev.append((top, 1))

        for x in special:
            ev.append((x - 1, 1))
            ev.append((x + 1, 0))

        ev.sort()
        # print(ev)
        last = None
        ans = 0
        for x, t in ev:
            if t == 0:
                last = x
            elif t == 1:
                if last is not None and x != last:
                    size = (x - last + 1)
                    ans = max(ans, size)
                last = None
        return ans

if __name__ == '__main__':
    pass
