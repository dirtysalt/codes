#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.seq = list(characters)
        self.pts = list(range(combinationLength))
        self.end = False

    def next(self) -> str:
        # print(self.pts)
        res = ''.join([self.seq[i] for i in self.pts])
        self.adjust_pts()
        return res

    def hasNext(self) -> bool:
        return not self.end

    def adjust_pts(self):
        pts, seq = self.pts, self.seq
        idx = len(self.pts) - 1

        while idx >= 0:
            p = pts[idx]
            if (p + len(pts) - idx) >= len(seq):
                idx -= 1
            else:
                self.pts[idx] += 1
                break

        if idx == -1:
            self.end = True
            return

        for i in range(idx + 1, len(self.pts)):
            self.pts[i] = self.pts[i - 1] + 1
