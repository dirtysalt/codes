#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import heapq


class LeftInt:
    def __init__(self, v):
        self.v = v

    def __lt__(self, other):
        return self.v >= other.v

    def value(self):
        return self.v


class RightInt:
    def __init__(self, v):
        self.v = v

    def __lt__(self, other):
        return self.v < other.v

    def value(self):
        return self.v


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left and self.left[0].value() >= num:
            heapq.heappush(self.left, LeftInt(num))
        else:
            heapq.heappush(self.right, RightInt(num))

        # 如果出现不平衡 size(left) - size(right) == 2
        # 或者是size(right) > size(left)
        if len(self.left) - len(self.right) == 2:
            x = heapq.heappop(self.left)
            heapq.heappush(self.right, RightInt(x.value()))
        elif len(self.right) > len(self.left):
            x = heapq.heappop(self.right)
            heapq.heappush(self.left, LeftInt(x.value()))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            x = self.left[0]
            return x.value()
        x = self.left[0]
        y = self.right[0]
        return (x.value() + y.value()) * 0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print((obj.findMedian()))
    obj.addNum(3)
    print((obj.findMedian()))
