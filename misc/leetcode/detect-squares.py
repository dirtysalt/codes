#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class DetectSquares:
    def __init__(self):
        from collections import defaultdict
        from collections import Counter
        self.xindex = defaultdict(list)
        self.yindex = defaultdict(list)
        self.cnt = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        key = (x, y)
        self.cnt[key] += 1
        self.xindex[x].append(key)
        self.yindex[y].append(key)

    def count(self, point: List[int]) -> int:
        x, y = point
        # search same y.
        ans = 0
        for x2, y2 in self.yindex[y]:
            d = x2 - x
            if d == 0: continue
            if True:
                x3, y3 = x2, y2 - d
                x4, y4 = x, y3
                ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]
            if True:
                x3, y3 = x2, y2 + d
                x4, y4 = x, y3
                ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

if __name__ == '__main__':
    pass
