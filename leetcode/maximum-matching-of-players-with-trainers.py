#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = 0
        ans = 0
        for x in players:
            while j < len(trainers) and x > trainers[j]: j += 1
            if j == len(trainers): break
            ans += 1
            j += 1
        return ans


if __name__ == '__main__':
    pass
