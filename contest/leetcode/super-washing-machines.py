#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# FIXME(yan): WA

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        sv = sum(machines)
        n = len(machines)
        if sv % n != 0:
            return -1
        avg = sv // n
        if all((x == avg for x in machines)):
            return 0

        sv = 0
        pivot = 0
        for i in range(n):
            sv += machines[i]
            if (i + 1) * avg <= sv:
                pivot = i
                break

        # [0..i] and [i..]
        def fx(xs):
            value = 0
            for i in range(len(xs)):
                if xs[i] < avg:
                    value = max(avg - xs[i] + i, value)
            return value

        a = fx(machines[:pivot + 1][::-1])
        b = fx(machines[pivot:])
        return max(a, b)


def test():
    cases = [
        ([1, 0, 5], 3),
        ([0, 3, 0], 2),
        ([0, 2, 0], -1),
        ([0, 0, 0, 4], 3)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (ms, exp) = c
        res = sol.findMinMoves(ms)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
