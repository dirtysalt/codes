#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        end = []
        for i in range(n):
            end.append((0, i))

        cnt = [0] * n
        for s, e in meetings:
            import heapq

            # many rooms are free, we have to reset end time.
            reset = []
            while end and end[0][0] <= s:
                reset.append(heapq.heappop(end)[1])
            for x in reset:
                heapq.heappush(end, (s, x))

            # find earliest free room.
            t, room = heapq.heappop(end)
            assert t >= s
            cnt[room] += 1
            heapq.heappush(end, (t + (e - s), room))

        target = max(cnt)
        for i in range(n):
            if cnt[i] == target:
                return i


true, false, null = True, False, None
cases = [
    (2, [[0, 10], [1, 5], [2, 7], [3, 4]], 0),
    (3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 1),
    (4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().mostBooked, cases)

if __name__ == '__main__':
    pass
