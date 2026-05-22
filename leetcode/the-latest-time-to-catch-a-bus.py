#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        j = 0
        ans = 1
        for b in buses:
            tmp = []
            for i in range(capacity):
                if j < len(passengers) and b >= passengers[j]:
                    tmp.append(passengers[j])
                    j += 1
                else:
                    break
            if len(tmp) < capacity:
                ans = b
            else:
                ans = tmp[-1] - 1

        mask = set(passengers)
        while ans in mask:
            ans -= 1
        return ans


true, false, null = True, False, None
cases = [
    ([10, 20], [2, 17, 18, 19], 2, 16),
    ([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2, 20),
    ([3], [2, 4], 2, 3),
    ([2], [2], 2, 1),
    ([3], [4], 1, 3),
    ([2, 4], [3, 4], 2, 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().latestTimeCatchTheBus, cases)

if __name__ == '__main__':
    pass
