#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]: return 0
        currentEnergy += sum(enemyEnergies) - enemyEnergies[0]
        return currentEnergy // enemyEnergies[0]


if __name__ == '__main__':
    pass
