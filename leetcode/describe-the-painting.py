#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = []

        for f, t, c in segments:
            events.append((f, 0, c))
            events.append((t, 1, c))
        events.sort()

        ans = []
        last = events[0][0]
        acc = 0
        for pos, ev, c in events:
            if last != pos:
                ans.append((last, pos, acc))
                last = pos

            if ev == 0:
                acc += c
            else:
                acc -= c

        ans = [t for t in ans if t[-1] != 0]
        return ans


if __name__ == '__main__':
    pass
