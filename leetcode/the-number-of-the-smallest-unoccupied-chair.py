#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        n = len(times)

        for i in range(n):
            f, t = times[i]
            events.append((f, 1, i))
            events.append((t, 0, i))

        events.sort()

        import heapq
        hp = list(range(n))
        taken = [-1] * n

        for t, ev, index in events:
            if ev == 0:
                seat = taken[index]
                heapq.heappush(hp, seat)
                taken[index] = -1

            else:
                seat = heapq.heappop(hp)
                taken[index] = seat
                if index == targetFriend:
                    return seat


if __name__ == '__main__':
    pass
