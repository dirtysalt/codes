#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24

if __name__ == '__main__':
    pass
