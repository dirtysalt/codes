#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cost = 0
        pos = [0] * 3

        dist = [0] * (len(travel) + 1)
        for i in range(len(travel)):
            dist[i + 1] += travel[i] + dist[i]

        for i in range(len(garbage)):
            for c in garbage[i]:
                if c == 'M':
                    idx = 0
                elif c == 'P':
                    idx = 1
                elif c == 'G':
                    idx = 2

                cost += 1
                pos[idx] = i

        for i in range(3):
            cost += dist[pos[i]]
        return cost


if __name__ == '__main__':
    pass
