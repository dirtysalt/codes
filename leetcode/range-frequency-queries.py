#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        from collections import defaultdict
        dist = defaultdict(list)
        for i in range(len(arr)):
            x = arr[i]
            dist[x].append(i)
        self.dist = dist

    def count(self, index, value):
        if index == -1:
            return 0
        ps = self.dist[value]
        import bisect
        return bisect.bisect_right(ps, index)

    def query(self, left: int, right: int, value: int) -> int:
        a = self.count(left - 1, value)
        b = self.count(right, value)
        return b - a


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

if __name__ == '__main__':
    pass
