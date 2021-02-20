#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        res = 0
        while i < j:
            if (people[j] + people[i]) <= limit:
                i, j = i + 1, j - 1
            else:
                j = j - 1
            res += 1
        if i == j:
            res += 1
        return res


def test():
    cases = [
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4, ], 5, 4)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (p, limit, exp) = c
        res = sol.numRescueBoats(p, limit)
        if res != exp:
            print('case failed. {}'.format(c))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
