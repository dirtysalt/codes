#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lhq = []
        self.rhq = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # insert first.
        if self.rhq and num >= self.rhq[0]:
            heapq.heappush(self.rhq, num)
        else:
            heapq.heappush(self.lhq, -num)
        # then balance.
        if len(self.rhq) - len(self.lhq) == 2:
            v = heapq.heappop(self.rhq)
            heapq.heappush(self.lhq, -v)
        elif len(self.lhq) - len(self.rhq) == 1:
            v = heapq.heappop(self.lhq)
            heapq.heappush(self.rhq, -v)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.rhq) == len(self.lhq):
            if len(self.lhq) == 0:
                return 0.0
            return (self.rhq[0] - self.lhq[0]) * 0.5
        else:
            return self.rhq[0]


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
