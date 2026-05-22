#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.counts = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        x = carType - 1
        if self.counts[x] > 0:
            self.counts[x] -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
