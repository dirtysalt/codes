#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# 这个可以处理非连续的版本
# 先对chargeTime进行排序，然后不断地插入costs
# 然后就是选择前缀和最小的costs, 不过好像没有特别好的数据结构
# 我这里的处理方法是，基于之前的k, 然后在附近进行线性搜索。
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        robots = list(zip(chargeTimes, runningCosts))
        robots.sort(key=lambda x: x[0])

        ans = 0
        from sortedcontainers import SortedList
        sl = SortedList()

        acc, k = 0, 0
        # print(robots)
        for i in range(len(robots)):
            time, cost = robots[i]

            if time + cost <= budget:
                while k < len(sl) and (time + (acc + cost) * (k + 1)) <= budget:
                    acc += sl[k]
                    k += 1

                while k >= 1 and (time + (acc + cost) * (k + 1)) > budget:
                    k -= 1
                    acc -= sl[k]

                ans = max(ans, k + 1)
            index = sl.bisect(cost)
            if index < k:
                acc += cost
                k += 1
            sl.add(cost)
            # assert acc == sum(sl[:k])

        return ans


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        from sortedcontainers import SortedList
        sl = SortedList()

        robots = list(zip(chargeTimes, runningCosts))
        j = 0
        tc = 0
        ans = 0
        for i in range(len(robots)):
            t, c = robots[i]
            sl.add(t)
            tc += c

            while j <= i and sl[-1] + (i - j + 1) * tc > budget:
                t, c = robots[j]
                sl.remove(t)
                tc -= c
                j += 1

            size = (i - j + 1)
            ans = max(ans, size)
        return ans


true, false, null = True, False, None
cases = [
    ([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25, 3),
    ([11, 12, 19], [10, 8, 7], 19, 0),
    ([11, 12, 74, 67, 37, 87, 42, 34, 18, 90, 36, 28, 34, 20], [18, 98, 2, 84, 7, 57, 54, 65, 59, 91, 7, 23, 94, 20],
     937, 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumRobots, cases)

if __name__ == '__main__':
    pass
