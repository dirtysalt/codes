#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def leastInterval(self, tasks, n):
#         """
#         :type tasks: List[str]
#         :type n: int
#         :rtype: int
#         """
#
#         cnt = [0] * 26
#         for t in tasks:
#             cnt[ord(t) - ord('A')] += 1
#
#         ans = 0
#         cnt.sort(key=lambda x: -x)
#         while True:
#             count = 0
#             for i in range(26):
#                 if cnt[i] == 0:
#                     break
#                 ans += 1
#                 cnt[i] -= 1
#                 count += 1
#                 if count == (n + 1):
#                     break
#
#             cnt.sort(key=lambda x: -x)
#             if cnt[0] == 0: break
#             if count < (n + 1):
#                 ans += (n + 1 - count)
#         return ans

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        cnt = [0] * 26
        for t in tasks:
            cnt[ord(t) - ord('A')] += 1

        # 维护一个最小堆，表示下一个可以运行的任务时间
        hp = [(0, cnt[i], chr(i + ord('A'))) for i in range(26) if cnt[i]]
        import heapq
        heapq.heapify(hp)

        ans = 0
        t0 = 0
        trace = []
        while len(hp):
            (t, c, ch) = hp[0]
            # 如果下一个可以运行的任务还没有到时的话，那么模拟延长
            delta = t - t0
            if delta > 0:
                ans += delta
                t0 += delta
                trace.extend(['idle'] * delta)

            assert t <= t0
            ans += 1
            t0 += 1
            trace.append(ch)
            if c > 1:
                # 下一次任务执行时间是t + n + 1, 还需要执行 c-1次
                heapq.heapreplace(hp, (t + n + 1, c - 1, ch))
            else:
                heapq.heappop(hp)

        # print(trace)
        return ans


cases = [
    (["A", "A", "A", "B", "B", "B"], 2, 8),
    (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().leastInterval, cases)
