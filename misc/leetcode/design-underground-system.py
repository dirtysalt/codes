#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class UndergroundSystem:

    def __init__(self):
        from collections import defaultdict
        self.st = defaultdict(lambda: [0, 0])
        self.user = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        assert id in self.user
        (name, t0) = self.user[id]
        key = name + '.' + stationName
        value = self.st[key]
        value[0] += 1
        value[1] += (t - t0)
        self.st[key] = value
        # del self.user[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + '.' + endStation
        value = self.st[key]
        return round(value[1] / value[0], 5)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
