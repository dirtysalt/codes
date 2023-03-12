#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        S = min((x[0] for x in tasks))
        E = max((x[1] for x in tasks))
        N = (E - S + 1)

        TS = set(range(S, E + 1))
        ans = 0
        while tasks:
            ev = []
            for s, e, d in tasks:
                ev.append((s, 0))
                ev.append((e + 1, 1))
            for t in TS:
                ev.append((t, 2))
            ev.sort()

            d = 0
            dm, tm = 0, 0
            for ts, ty in ev:
                if ty == 0:
                    d += 1
                elif ty == 1:
                    d -= 1
                else:
                    if d > dm:
                        dm = d
                        tm = ts

            # print('use tm ', tm)
            TS.remove(tm)
            ans += 1

            tmp = []
            for s, e, d in tasks:
                if s <= tm <= e:
                    d -= 1
                    if d > 0:
                        tmp.append((s, e, d))
                else:
                    tmp.append((s, e, d))
            tasks = tmp

        return ans


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        run = [False] * 2001
        tasks.sort(key=lambda x: x[1])

        for s, e, d in tasks:
            d -= sum(run[s:e + 1])  # 这段时间内之前已经被安排了多少，这个可以附带上
            if d > 0:
                for t in reversed(range(s, e + 1)):  # 剩余的时间从后往前安排
                    if run[t]: continue
                    d -= 1
                    run[t] = True
                    if d == 0: break

        return sum(run)


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[2, 3, 1], [4, 5, 1], [1, 5, 2]], 2),
    ([[1, 3, 2], [2, 5, 3], [5, 6, 2]], 4),
    ([[68, 129, 2], [58, 86, 9], [112, 142, 10], [106, 108, 1], [48, 48, 1], [116, 143, 2], [28, 43, 5], [1, 1, 1],
      [75, 83, 3], [104, 136, 10], [11, 11, 1], [60, 63, 1], [73, 111, 8], [57, 57, 1], [117, 119, 3], [25, 38, 2],
      [20, 21, 1], [78, 80, 2], [17, 17, 1], [28, 28, 1], [77, 117, 3], [76, 109, 4], [61, 61, 1], [84, 92, 5],
      [18, 41, 4], [47, 55, 9], [74, 132, 6], [53, 87, 3], [102, 131, 7], [26, 26, 1], [66, 68, 3], [59, 73, 1],
      [22, 30, 9], [9, 13, 2], [31, 35, 2], [90, 91, 2], [72, 72, 1], [62, 84, 8], [105, 106, 2], [3, 3, 1],
      [32, 32, 1], [99, 103, 4], [45, 52, 4], [108, 116, 3], [91, 123, 8], [89, 114, 4], [94, 130, 7], [103, 104, 2],
      [14, 17, 4], [63, 66, 4], [98, 112, 7], [101, 140, 9], [58, 58, 1], [109, 145, 1], [8, 15, 8], [4, 16, 5],
      [115, 141, 1], [40, 50, 4], [118, 118, 1], [81, 120, 7]], 68)
]

aatest_helper.run_test_cases(Solution().findMinimumTime, cases)

if __name__ == '__main__':
    pass
