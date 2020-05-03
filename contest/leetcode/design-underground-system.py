#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class UndergroundSystem:

    def __init__(self):
        from collections import Counter
        self.custom = {}
        self.path_sum = Counter()
        self.path_count = Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.custom[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        st0, t0 = self.custom[id]
        key = '{}.{}'.format(st0, stationName)
        value = t - t0
        self.path_sum[key] += value
        self.path_count[key] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = '{}.{}'.format(startStation, endStation)
        sum = self.path_sum[key]
        count = self.path_count[key]
        return sum * 1.0 / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
