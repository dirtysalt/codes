#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        import heapq
        hp = []
        current = [0] * (len(persons) + 1)
        tmp = []
        for (t, p) in zip(times, persons):
            current[p] += 1
            v = current[p]
            heapq.heappush(hp, (-v, -t, p))

            _, _, p0 = hp[0]
            tmp.append(p0)

        assert len(tmp) == len(times)
        print(tmp)
        self.tmp = tmp
        self.times = times

    def q(self, t: int) -> int:
        times = self.times

        def bs(t):
            s, e = 0, len(times) - 1
            while s <= e:
                m = (s + e) // 2
                if times[m] > t:
                    e = m - 1
                else:
                    s = m + 1
            return e

        idx = bs(t)
        return self.tmp[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

null = None
cases = [
    (["TopVotedCandidate", "q", "q", "q", "q", "q", "q"],
     [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]], [null, 0, 1, 1, 0, 0, 1])
]

import aatest_helper

aatest_helper.run_simulation_cases(TopVotedCandidate, cases)
